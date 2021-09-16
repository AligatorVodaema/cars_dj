from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class Car(models.Model):
    model = models.CharField(max_length=100, verbose_name='Модель')
    brand = models.CharField(max_length=100, verbose_name='Брэнд')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание')
    is_reserved = models.BooleanField(default=False, verbose_name='Зарезервировано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    cat = models.ForeignKey('CategoryCars', on_delete=models.PROTECT, verbose_name='Категории')
    car_owner = models.ForeignKey(User, on_delete=models.SET_NULL,
    null=True, blank=True, verbose_name='Пользователь')


    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = 'Прокатные Авто'
        verbose_name_plural = 'Прокатные Авто'
        ordering = ['id']


class CategoryCars(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории Авто'
        verbose_name_plural = 'Категории Авто'
        ordering = ['id']