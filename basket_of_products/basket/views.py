from typing import Any
from django.views.generic import TemplateView

from .models import Product


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
