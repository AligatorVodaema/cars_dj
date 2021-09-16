from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.forms.widgets import Select
from cars.package_services import db_services


class ReserveCarForm(forms.Form):
    """Select-menu with available autos."""
    brand = forms.ChoiceField(label='Брэнд')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].choices = db_services.get_and_zip_car_values(
            'pk', 'brand')



        
class RegisterUserForm(UserCreationForm):
    """Default Form for register new User"""
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    """Default Form for login User"""
    username = forms.CharField(label='Логин', 
        widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    """Form for Feedback"""
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    content = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 10}), max_length=100)
    captcha = CaptchaField()
