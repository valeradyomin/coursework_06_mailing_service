from django.shortcuts import render
import random
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from app_mailing.forms import MailingSrvForm, MailForm
from app_mailing.models import MailingSrv, Mail


# Create your views here.

class BaseContextMixin:
    phrases = [
        "Почтовая рассылка: отправка сообщений и уведомлений по электронной почте.",
        "Автоматизация рассылок: возможность настроить автоматическую отправку сообщений по определенным событиям "
        "или расписанию.",
        "Управление подписчиками: возможность добавлять и удалять подписчиков, управлять списками рассылок и "
        "сегментировать аудиторию.",
        "Шаблоны и персонализация: создание и использование шаблонов для удобного оформления сообщений, "
        "а также возможность персонализации контента для каждого получателя."
        "Аналитика и отчетность: предоставление статистики о доставке, открытии и кликах в сообщениях, "
        "а также возможность создания отчетов для оценки эффективности рассылок."
        "Сегментация аудитории: возможность разделить аудиторию на группы и отправлять сообщения только "
        "определенным сегментам."
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_phrase = random.choice(self.phrases)
        context['phrases'] = random_phrase
        return context


class MainPage(BaseContextMixin, TemplateView):
    template_name = 'app_mailing/home.html'
    extra_context = {
        'title': 'Главная страница нашего сайта',
        'phrases': BaseContextMixin.phrases,
    }


class MailingSrvListView(BaseContextMixin, ListView):
    model = MailingSrv
    extra_context = {
        'title': 'Список рассылок',
        'phrases': BaseContextMixin.phrases,
    }


class MailingSrvCreateView(BaseContextMixin, CreateView):
    model = MailingSrv
    form_class = MailingSrvForm

    success_url = reverse_lazy('app_mailing:mailings_list')

    extra_context = {
        'title': 'Создание новой рассылки',
        'phrases': BaseContextMixin.phrases,
    }


class MailingSrvUpdateView(BaseContextMixin, UpdateView):
    model = MailingSrv
    form_class = MailingSrvForm

    extra_context = {
        'title': 'Редактирование рассылки',
        'phrases': BaseContextMixin.phrases,
    }

    def get_success_url(self):
        return reverse('app_mailing:mailings_detail', args=[self.object.pk])


class MailingSrvDetailView(BaseContextMixin, DetailView):
    model = MailingSrv

    extra_context = {
        'title': 'Детали рассылки',
        'phrases': BaseContextMixin.phrases,
    }


class MailingSrvDeleteView(BaseContextMixin, DeleteView):
    model = MailingSrv
    success_url = reverse_lazy('app_mailing:mailings_list')

    extra_context = {
        'title': 'Удаление рассылки',
        'phrases': BaseContextMixin.phrases,
    }


class MailListView(BaseContextMixin, ListView):
    model = Mail
    extra_context = {
        'title': 'Список писем',
        'phrases': BaseContextMixin.phrases,
    }


class MailCreateView(BaseContextMixin, CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('app_mailing:mail_list')
    extra_context = {
        'title': 'Создание письма',
        'phrases': BaseContextMixin.phrases,
    }


class MailUpdateView(BaseContextMixin, UpdateView):
    model = Mail
    form_class = MailForm
    extra_context = {
        'title': 'Редактирование письма',
        'phrases': BaseContextMixin.phrases,
    }

    def get_success_url(self):
        return reverse('app_mailing:mail_detail', args=[self.kwargs.get('pk')])


class MailDetailView(BaseContextMixin, DetailView):
    model = Mail
    extra_context = {
        'title': 'Просмотр письма',
        'phrases': BaseContextMixin.phrases,
    }


class MailDeleteView(BaseContextMixin, DeleteView):
    model = Mail
    success_url = reverse_lazy('app_mailing:mail_list')
    extra_context = {
        'title': 'Удаление письма',
        'phrases': BaseContextMixin.phrases,
    }
