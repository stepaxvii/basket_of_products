from django.db import models
from django.contrib.auth import get_user_model
from .abstract import BaseModel


# Менеджер, способный создавать ресторан и продукты
User = get_user_model()


class Restaurant(BaseModel):
    """Модель ресторана/кафе."""

    name = models.CharField(
        max_length=50,
        verbose_name='Ресторан'
    )
    email = models.EmailField(
        max_length=50,
        verbose_name='Электронная почта',
        help_text='Укажите электронную почту ресторана.',
        null=True,
        blank=True
    )
    concept = models.TextField(
        verbose_name='Концепция',
        help_text=(
            'Опишите историю создания вашего заведения,'
            'его концепцию, особенности.\nВсё, чем оно уникально.'
        ),
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='restorants_images',
        blank=True
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'Ресторан'
        verbose_name_plural = 'рестораны'

    def __str__(self):
        return f'{self.name}'


class Category(BaseModel):
    """Модель категории блюд/напитков."""

    title = models.CharField(
        max_length=20,
        verbose_name='Категория'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        max_length=20,
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL;'
            ' разрешены символы латиницы, цифры, дефис и подчёркивание.\n'
            'Например: для раздела "Супы" подойдёт идентификатор "soups"'
        )
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Ресторан',
        related_name='categories'
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'категория {self.title}'


class Product(BaseModel):
    """Модель блюда/напитка."""

    title = models.CharField(
        verbose_name='Название в меню',
        max_length=40
    )
    ingredients = models.TextField(
        verbose_name='Состав'
    )
    allergens = models.TextField(
        verbose_name='Аллергены',
        blank=True
    )
    description = models.TextField(
        verbose_name='Процесс приготовления',
        blank=True
    )
    history = models.TextField(
        verbose_name='История',
        help_text='интересные факты или история создания',
        blank=True
    )
    weight = models.IntegerField(
        verbose_name='Выход',
        default=0,
        blank=True
    )
    price = models.IntegerField(
        verbose_name='Цена',
        default=0,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='products_images',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='products'
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Ресторан',
        related_name='products'
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'Продукт'
        verbose_name_plural = 'блюда/напитки'

    def __str__(self):
        return f'{self.title}'
