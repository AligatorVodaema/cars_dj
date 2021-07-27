from django.urls import path
from .views import CarHome, CarCategory, ShowCarPost


urlpatterns = [
    path('', CarHome.as_view(), name='home'),
    path('category/<slug:cat_slug>/', CarCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowCarPost.as_view(), name='post'),

]
