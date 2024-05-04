from django.views.generic import CreateView

from .forms import ProductForm
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'index.html'
