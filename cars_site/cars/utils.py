from django.db.models import Count
from django.core.cache import cache
from .models import *



menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Забронировать авто', 'url_name': 'reserve_menu'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
    ]



class DataMixin:
    
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = CategoryCars.objects.annotate(Count('car'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context