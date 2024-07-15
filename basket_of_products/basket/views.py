from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
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


def get_user_restaurants(user):
    """Фильтрация доступных пользователю объектов."""
    if user.is_authenticated:
        if user.is_superuser:
            return Restaurant.objects.all()
        return Restaurant.objects.filter(
            Q(manager=user) | Q(waiter=user)
        )
    return Restaurant.objects.none()


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
        return get_user_restaurants(self.request.user)


class RestaurantDetailView(DetailView):
    """CBV для отображения страницы ресторана."""

    model = Restaurant
    template_name = 'basket/restaurant-detail.html'

    def get_queryset(self):
        return Restaurant.objects.select_related('waiter', 'manager')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            restaurant=self.object
        ).order_by('-modified_at').select_related('category')
        context['categories'] = Category.objects.filter(
            restaurant=self.object
        ).prefetch_related('products')
        return context


class ProductDetailView(DetailView):
    """CBV для просмотра отдельного продукта."""
    model = Product
    template_name = 'basket/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CategoriesView(ListView):
    """CBV для отображения доступных категорий."""
    model = Category
    template_name = 'basket/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Category.objects.all()
            return Category.objects.filter(
                restaurant__manager=self.request.user
            ) | Category.objects.filter(
                restaurant__waiter=self.request.user
            )
        return Category.objects.all()


class CategoryDetailView(DetailView):
    """CBV для отображения отдельной категории."""
    model = Category
    template_name = 'basket/category-detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            category=self.object,
            restaurant=self.object.restaurant
        )
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
        return reverse(
            'basket:restaurant-detail',
            kwargs={'pk': self.object.restaurant.pk}
        )


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


class LastChangesProductView(ListView):
    """CBV для отображения последних добавленных/изменённых продуктов"""

    model = Product
    template_name = 'basket/last-changes.html'
    context_object_name = 'products'

    def get_queryset(self):
        restaurants = get_user_restaurants(self.request.user)
        return Product.objects.filter(
            restaurant__in=restaurants
        ).order_by('-modified_at')
