from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, ListView

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
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация пользователя',
        'phrases': BaseContextMixin.phrases,
    }

    def form_valid(self, form):
        password = User.objects.make_random_password()
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.verification_code = password
        new_user.save()

        current_site = get_current_site(self.request)
        url = f'http://{current_site}/users/email_verify/{new_user.verification_code}/'

        send_mail(
            recipient_list=[new_user.email],
            subject='Подтвердите ваш почтовый адрес',
            message=f'Для завершения регистрации на сайте перейдите по ссылке: {url}',
            from_email=settings.EMAIL_HOST_USER,
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:verification_check') + f'?email={self.object.email}'


class RegisterInfo(TemplateView):
    template_name = 'users/verification_check.html'

    extra_context = {
        'title': 'Подтвердите регистрацию',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_email = self.request.GET.get('email')
        context['info'] = f'На ваш почтовый адрес {user_email} была отправлена ссылка для завершения регистрации.'
        return context


class UserListView(BaseContextMixin, ListView):
    model = User
    extra_context = {
        'title': 'Список пользователей сервиса',
        'phrases': BaseContextMixin.phrases,
    }


def get_verification(request, verification_code):
    try:
        user = User.objects.filter(verification_code=verification_code).first()
        user.is_active = True
        user.save()
        return redirect('users:verification_approve')
    except (AttributeError, ValidationError):
        return redirect('users:verification_reject')
