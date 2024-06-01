from django.views.generic import ListView

from .models import Restoran, Product


class HomePageView(ListView):
    """CBV для отображения главной страницы."""

    template_name = 'basket/index.html'
    model = Restoran
    context_object_name = 'restorans'
    paginate_by = 3


class RestoranView(ListView):
    """CBV для отображение выбранного ресторана."""

    template_name = 'basket/restoran.html'
    model = Product
    context_object_name = 'restorans'
    paginate_by = 3
