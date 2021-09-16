from django.urls import path
from .views import *
from .auth_view import RegisterUserView, LoginUserView, logout_user

urlpatterns = [
    path('', CarHome.as_view(), name='home'),
    path('category/<slug:cat_slug>/', CarCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowCarPost.as_view(), name='post'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('reserve_menu/', ReserveCarView.as_view(), name='reserve_menu'),
    path('logout/', logout_user, name='logout'),
    path('about/', show_info_about_site, name='about'),
    path('make_reserve/', make_reserve, name='make_reserve'),


]
