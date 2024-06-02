from django.views.generic import ListView

from .models import Restaurant, Product


class HomePageView(ListView):
    """CBV для отображения главной страницы."""

    template_name = 'basket/index.html'
    model = Restaurant
    context_object_name = 'restaurants'
    paginate_by = 2


class RestaurantView(ListView):
    """CBV для отображение выбранного ресторана."""

    template_name = 'basket/restaurant.html'
    model = Restaurant
    context_object_name = 'restaurant'
    paginate_by = 3
