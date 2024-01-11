from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app_mailing.views import BaseContextMixin
from users.forms import LoginViewForm, UserRegisterForm
from users.models import User


# Create your views here.


class LoginView(BaseContextMixin, BaseLoginView):
    model = User
    form_class = LoginViewForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Вход пользователя',
        'phrases': BaseContextMixin.phrases,
    }


class LogoutView(BaseLogoutView):
    pass


class RegisterView(BaseContextMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verification_code')
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация пользователя',
        'phrases': BaseContextMixin.phrases,
    }
