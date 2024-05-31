from django.views.generic import ListView

from .models import Restoran


class HomePageView(ListView):
    """CBV для отображения главной страницы."""

    template_name = 'basket/index.html'
    model = Restoran
    context_object_name = 'restorans'
    paginate_by = 3
