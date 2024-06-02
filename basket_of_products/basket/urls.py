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
        views.RestaurantView.as_view(),
        name='restaurant-detail'
    ),
]
