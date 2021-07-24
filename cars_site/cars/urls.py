from django.urls import path
from .views import CarHome


urlpatterns = [
    path('', CarHome.as_view(), name='home')
]
