from django.contrib import admin

from .models import Category, Product, Restaurant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Регистрация модели Категории в админке."""

    list_display = (
        'title',
        'created_at'
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'created_at',
    )
    ordering = (
        '-created_at',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Регистрация модели Категории в админке."""

    list_display = (
        'title',
        'created_at'
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'created_at',
    )
    ordering = (
        '-created_at',
    )


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Регистрация модели Ресторан в админке."""

    list_display = (
        'name',
        'created_at'
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'created_at',
    )
    ordering = (
        '-created_at',
    )
