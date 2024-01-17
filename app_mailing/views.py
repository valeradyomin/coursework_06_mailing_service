from django.shortcuts import render
import random
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from app_blog.models import Blogpost
from app_mailing.forms import MailingSrvForm, MailForm, ClientForm
from app_mailing.models import MailingSrv, Mail, Client, Log


from users.models import User


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
        'phrases': BaseContextMixin.phrases,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница нашего сайта'
        context['mailings_count'] = MailingSrv.objects.count()
        context['created_mailings_count'] = MailingSrv.objects.filter(status='создана').count()
        context['processing_mailings_count'] = MailingSrv.objects.filter(status='запущена').count()
        context['finished_mailings_count'] = MailingSrv.objects.filter(status='завершена').count()
        context['unique_clients_count'] = Client.objects.count()
        context['unique_users_count'] = User.objects.count()

        blogpost_list = list(Blogpost.objects.all())
        random.shuffle(blogpost_list)
        context['blogpost_list'] = blogpost_list[:3]

        return context


class MailingSrvListView(BaseContextMixin, ListView):
    model = MailingSrv
    extra_context = {
        'title': 'Список рассылок',
        'phrases': BaseContextMixin.phrases,
    }


class MailingSrvCreateView(BaseContextMixin, CreateView):
    model = MailingSrv
    form_class = MailingSrvForm

    extra_context = {
        'title': 'Создание новой рассылки',
        'phrases': BaseContextMixin.phrases,
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form, *args, **kwargs):
        if form.is_valid():
            new_mailing = form.save(commit=False)
            new_mailing.owner = self.request.user
            new_mailing.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_mailing:mailings_list')


class MailingSrvUpdateView(BaseContextMixin, UpdateView):
    model = MailingSrv
    form_class = MailingSrvForm

    extra_context = {
        'title': 'Редактирование рассылки',
        'phrases': BaseContextMixin.phrases,
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_success_url(self):
        return reverse('app_mailing:mailings_detail', args=[self.object.pk])


class MailingSrvDetailView(BaseContextMixin, DetailView):
    model = MailingSrv

    extra_context = {
        'title': 'Детали рассылки',
        'phrases': BaseContextMixin.phrases,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_data = []
        recipients_data = self.object.recipients.values('email', 'initials', 'comment')
        mailing_data.append({'recipients_data': recipients_data})
        context['mailing_data'] = mailing_data
        return context


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

    def form_valid(self, form):
        new_mail = form.save()
        new_mail.owner = self.request.user
        new_mail.save()
        return super().form_valid(form)


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


class ClientListView(BaseContextMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Список клиентов',
        'phrases': BaseContextMixin.phrases,
    }


class ClientCreateView(BaseContextMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('app_mailing:client_list')
    extra_context = {
        'title': 'Добавить клиента',
        'phrases': BaseContextMixin.phrases,
    }

    def form_valid(self, form):
        new_client = form.save()
        new_client.owner = self.request.user
        new_client.save()
        return super().form_valid(form)


class ClientUpdateView(BaseContextMixin, UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Редактирование клиента',
        'phrases': BaseContextMixin.phrases,
    }

    def get_success_url(self):
        return reverse('app_mailing:client_detail', args=[self.kwargs.get('pk')])


class ClientDetailView(BaseContextMixin, DetailView):
    model = Client
    extra_context = {
        'title': 'Просмотр клиента',
        'phrases': BaseContextMixin.phrases,
    }


class ClientDeleteView(BaseContextMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('app_mailing:client_list')
    extra_context = {
        'title': 'Удаление клиента',
        'phrases': BaseContextMixin.phrases,
    }


class LogListView(BaseContextMixin, ListView):
    model = Log
    extra_context = {
        'title': 'Отчеты по рассылкам',
        'phrases': BaseContextMixin.phrases,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_data = []
        for log in context['object_list']:
            recipients_data = log.mailing.recipients.values('email', 'initials', 'comment')
            mailing_data.append({'log': log, 'recipients_data': recipients_data})
        context['mailing_data'] = mailing_data
        return context


class LogDetailView(BaseContextMixin, DetailView):
    model = Log
    extra_context = {
        'title': 'Отчет по рассылке',
        'phrases': BaseContextMixin.phrases,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_data = []
        recipients_data = self.object.mailing.recipients.values('email', 'initials', 'comment')
        mailing_data.append({'log': self.object, 'recipients_data': recipients_data})
        context['mailing_data'] = mailing_data
        return context


class LogDeleteView(BaseContextMixin, DeleteView):
    model = Log
    success_url = reverse_lazy('app_mailing:log_list')
    extra_context = {
        'title': 'Удаление отчета',
        'phrases': BaseContextMixin.phrases,
    }
