from typing import Any

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView
)

from .models import Category, Restaurant, Product
from .forms import CategoryForm, ProductForm


class HomePageView(TemplateView):
    """CBV для отображения главной страницы."""

    template_name = 'basket/index.html'


class RestaurantsView(ListView):
    """CBV для отображения доступных пользователю ресторанов."""

    model = Restaurant
    template_name = 'basket/restaurants.html'
    context_object_name = 'restaurants'
    paginate_by = 2

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Restaurant.objects.all()
            return Restaurant.objects.filter(waiter=self.request.user)
        return Restaurant.objects.all()


class RestaurantDetailView(DetailView):
    """CBV для отображения страницы ресторана."""

    model = Restaurant
    template_name = 'basket/restaurant-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            restaurant=self.object
        ).order_by('-modified_at')
        context['categories'] = Category.objects.filter(restaurant=self.object)
        return context


class ProductDetailView(DetailView):
    """CBV для просмотра отдельного продукта."""
    model = Product
    template_name = 'basket/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(
    user_passes_test(lambda u: u.is_staff or u.is_superuser),
    name='dispatch'
)
class ProductCreateView(CreateView):
    """CBV форма для создания нового продукта."""
    model = Product
    form_class = ProductForm
    template_name = 'basket/product-create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('basket:product-detail', kwargs={'pk': self.object.pk})


@method_decorator(
    user_passes_test(lambda u: u.is_staff or u.is_superuser),
    name='dispatch'
)
class CategoryCreateView(CreateView):
    """CBV форма для создания нового продукта."""
    model = Category
    form_class = CategoryForm
    template_name = 'basket/category-create.html'

    def get_success_url(self):
        return reverse(
            'basket:restaurant-detail',
            kwargs={'pk': self.object.restaurant.pk}
        )
