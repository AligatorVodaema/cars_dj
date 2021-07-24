from django.shortcuts import render
from .models import Car, CategoryCars
from .utils import DataMixin
from django.views.generic import ListView
from django.http.response import HttpResponseNotFound


class CarHome(DataMixin, ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Car.objects.filter(is_published=True).select_related('cat')


class CarCategory(DataMixin, ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = CategoryCars.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена :(</h1>')