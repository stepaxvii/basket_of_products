from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Category, Restaurant, Product


class HomePageView(ListView):
    """CBV для отображения главной страницы."""

    model = Restaurant
    template_name = 'basket/index.html'
    context_object_name = 'restaurants'
    paginate_by = 2

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Restaurant.objects.all()
        return Restaurant.objects.filter(waiter=self.request.user)


class RestaurantDetailView(DetailView):
    """CBV для отображения страницы ресторана."""

    model = Restaurant
    template_name = 'basket/restaurant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            restaurant=self.object
        ).order_by('-modified_at')
        context['categories'] = Category.objects.filter(restaurant=self.object)
        return context
