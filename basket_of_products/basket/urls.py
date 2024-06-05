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
        'restaurant/<int:pk>',
        views.RestaurantDetailView.as_view(),
        name='restaurant'
    ),
]
