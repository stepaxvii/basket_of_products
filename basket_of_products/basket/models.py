from django.db import models

from .abstract import BaseModel


class Category(BaseModel):
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
            'Например: для раздела "Супы" подойдёт идентификатор "soup"'
        )
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'раздел меню'
        verbose_name_plural = 'Разделы меню (категории)'

    def __str__(self):
        return self.title


class Product(BaseModel):
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

    class Meta(BaseModel.Meta):
        verbose_name = 'Продукт'
        verbose_name_plural = 'блюда/напитки'

    def __str__(self):
        return self.title
