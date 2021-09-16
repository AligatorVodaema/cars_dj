from django.shortcuts import render, redirect
from .models import Car, CategoryCars
from .utils import DataMixin
from django.views.generic import ListView, DetailView, View
from django.http.response import HttpResponse, HttpResponseNotFound
from .forms import *
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from cars.package_services import db_services



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
        return Car.objects.filter(is_published=True, 
            is_reserved=False).select_related('cat')


class CarCategory(DataMixin, ListView):
    """View for left side bar on main page.
    Send category_pk for correct display categories."""
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = CategoryCars.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name), 
            cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], 
            is_published=True).select_related('cat')


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

    def post(self, request):
        print('*' * 20, dir(redirect))
        print('*' * 20, request.POST)
        


class ContactFormView(DataMixin, FormView):
    """View for FeedBack Form"""
    form_class = ContactForm
    template_name = 'cars/contact.html'
    success_url = reverse_lazy('home')
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class ReserveCarView(LoginRequiredMixin, DataMixin, View):
    """View for reserv auto form."""

    def get(self, request):
        '''On method get request, provides form for car selection.'''
        form = ReserveCarForm()
        context = self.get_user_context(title='Бронировать Авто', form=form)

        return render(request=request, template_name='cars/menu_reserv_auto.html', 
            context=context)


    def post(self, request):
        '''Method post. Redicrect to selected car-post.'''
        pk = request.POST.get('brand')
        qs = Car.objects.get(pk=pk)

        return redirect(qs.get_absolute_url())


def make_reserve(request):
    return HttpResponse('<h1>OK</h1>')


def show_info_about_site(reqest):
    return HttpResponse('<h1>INFO</h1>')



def pageNotFound(request, exception):
    """Func for nice 404 response"""
    return HttpResponseNotFound('<h1> Страница не найдена :(</h1>')