from django.db import models

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

    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name = 'Прокатные авто'
        verbose_name_plural = 'Прокатные авто'
        ordering = ['id']


class CategoryCars(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']