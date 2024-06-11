from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.urls import reverse

from .models import Category, Restaurant, Product


class HomePageView(ListView):
    """CBV для отображения главной страницы."""

    model = Restaurant
    template_name = 'basket/index.html'
    context_object_name = 'restaurants'
    paginate_by = 2

    # В таком случае не проходит отображение страницы,
    # если юзер не залогинился.
    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Restaurant.objects.all()
            return Restaurant.objects.filter(waiter=self.request.user)

    # Тут отдельный оф видит все ресты!
        def get(self, request):
            if not request.user.is_authenticated:
                return redirect('pages:about')
            if request.user.is_superuser:
                restaurants = Restaurant.objects.all()
            else:
                restaurants = Restaurant.objects.filter(waiter=request.user)
            return super().get(request, restaurants)
# Объеденить эти две функции в одну


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
