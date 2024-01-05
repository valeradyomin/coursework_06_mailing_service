from django.urls import path

from app_mailing.apps import AppMailingConfig
from app_mailing.views import MainPage, MailingSrvListView, MailingSrvCreateView, MailingSrvUpdateView, \
    MailingSrvDetailView, MailingSrvDeleteView, MailListView, MailCreateView, MailUpdateView, MailDetailView, \
    MailDeleteView, ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView

app_name = AppMailingConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('mailings_list/', MailingSrvListView.as_view(), name='mailings_list'),
    path('mailings_create/', MailingSrvCreateView.as_view(), name='mailings_create'),
    path('mailings_update/<int:pk>/', MailingSrvUpdateView.as_view(), name='mailings_update'),
    path('mailings_detail/<int:pk>/', MailingSrvDetailView.as_view(), name='mailings_detail'),
    path('mailings_delete/<int:pk>/', MailingSrvDeleteView.as_view(), name='mailings_delete'),
    path('mail_list/', MailListView.as_view(), name='mail_list'),
    path('mail_create/', MailCreateView.as_view(), name='mail_create'),
    path('mail_update/<int:pk>/', MailUpdateView.as_view(), name='mail_update'),
    path('mail_detail/<int:pk>/', MailDetailView.as_view(), name='mail_detail'),
    path('mail_delete/<int:pk>/', MailDeleteView.as_view(), name='mail_delete'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
