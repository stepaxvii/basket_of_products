from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, TemplateView

from .models import Category, Restaurant, Product


class HomePageView(TemplateView):
    """CBV для отображения главной страницы."""

    template_name = 'basket/index.html'


class RestaurantsView(ListView):
    """CBV для отображения доступных пользователю ресторанов."""

    model = Restaurant
    template_name = 'basket/restaurants.html'
    context_object_name = 'restaurants'
    paginate_by = 2

    # В таком случае не проходит отображение страницы,
    # если юзер не залогинился.
    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Restaurant.objects.all()
            return Restaurant.objects.filter(waiter=self.request.user)
        return Restaurant.objects.all()


class RestaurantDetailView(DetailView):
    """CBV для отображения страницы ресторана."""

    model = Restaurant
    template_name = 'basket/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            restaurant=self.object
        ).order_by('-modified_at')
        context['categories'] = Category.objects.filter(restaurant=self.object)
        return context
