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
        'restoran/<int:pk>',
        views.RestoranView.as_view(),
        name='restoran'
    ),
]
