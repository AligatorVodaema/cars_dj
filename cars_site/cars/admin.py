from django.contrib import admin
from .models import Car, CategoryCars
from django.utils.safestring import mark_safe


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'time_create', 'get_html_photo',
     'is_published', 'is_reserved', 'slug')
    list_display_links = ('id', 'model', 'brand', 'slug')
    search_fields = ('model', 'brand', 'description')
    list_editable = ('is_published', 'is_reserved')
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("model",)}
    fields = ('model', 'brand', 'slug', 'cat', 'description', 'photo', 'get_html_photo',
     'is_published', 'time_create', 'is_reserved')
    readonly_fields = ('time_create', 'get_html_photo')
    save_on_top = True
    

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

    get_html_photo.short_description = 'Миниатюра'

class CategoryCarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    

admin.site.register(Car, CarAdmin)
admin.site.register(CategoryCars, CategoryCarsAdmin)