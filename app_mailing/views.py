from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from app_mailing.models import MailingSrv


# Create your views here.


class MainPage(TemplateView):
    template_name = 'app_mailing/base.html'


class MailingSrvListView(ListView):
    model = MailingSrv
