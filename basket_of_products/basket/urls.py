from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path(
        '',
        views.HomePageView.as_view(),
        name='index'
    ),
    path(
        'restaurants',
        views.RestaurantsView.as_view(),
        name='restaurants'
    ),
    path(
        'restaurant/<int:pk>',
        views.RestaurantDetailView.as_view(),
        name='restaurant-detail'
    ),
    path(
        'product/<int:pk>',
        views.ProductDetailView.as_view(),
        name='product-detail'
    ),
    path(
        'product-create',
        views.ProductCreateView.as_view(),
        name='product-create'
    ),
    path(
        'category-create',
        views.CategoryCreateView.as_view(),
        name='category-create'
    ),
]
