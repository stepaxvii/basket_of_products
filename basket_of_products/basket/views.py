from django.views.generic import ListView
from .models import Restoran


class HomePageView(ListView):
    """CBV для отображения главной страницы."""

    template_name = 'index.html'
    model = Restoran
    context_object_name = 'restorans'  # Имя переменной контекста для передачи списка ресторанов
    paginate_by = 3  # Количество ресторанов на одной странице
