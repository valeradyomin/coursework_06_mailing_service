from django.urls import path

from app_mailing.apps import AppMailingConfig
from app_mailing.views import MainPage, MailingSrvListView, MailingSrvCreateView

app_name = AppMailingConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('mailings_list/', MailingSrvListView.as_view(), name='mailings_list'),
    path('mailings_create/', MailingSrvCreateView.as_view(), name='mailings_create'),
]
