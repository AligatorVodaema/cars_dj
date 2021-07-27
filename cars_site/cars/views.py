from django.shortcuts import render
from .models import Car, CategoryCars
from .utils import DataMixin
from django.views.generic import ListView, DetailView
from django.http.response import HttpResponseNotFound


class CarHome(DataMixin, ListView):
    """View for only published and not reserved cars on main page"""
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Car.objects.filter(is_published=True, is_reserved=False).select_related('cat')


class CarCategory(DataMixin, ListView):
    """View for left side bar on main page. Send category_pk for correct display categories."""
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = CategoryCars.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class ShowCarPost(DataMixin, DetailView):
    """Show detail about turned car."""
    model = Car
    template_name = 'cars/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена :(</h1>')