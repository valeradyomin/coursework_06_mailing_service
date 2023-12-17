from django.urls import path

from app_mailing.apps import AppMailingConfig
from app_mailing.views import MainPage, MailingSrvListView, MailingSrvCreateView, MailingSrvUpdateView, \
    MailingSrvDetailView, MailingSrvDeleteView

app_name = AppMailingConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('mailings_list/', MailingSrvListView.as_view(), name='mailings_list'),
    path('mailings_create/', MailingSrvCreateView.as_view(), name='mailings_create'),
    path('mailings_update/<int:pk>/', MailingSrvUpdateView.as_view(), name='mailings_update'),
    path('mailings_detail/<int:pk>/', MailingSrvDetailView.as_view(), name='mailings_detail'),
    path('mailings_delete/<int:pk>/', MailingSrvDeleteView.as_view(), name='mailings_delete'),
]
