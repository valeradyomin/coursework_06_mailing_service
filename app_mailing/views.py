from django.shortcuts import render
import random
from django.views.generic import TemplateView, ListView

from app_mailing.models import MailingSrv


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
