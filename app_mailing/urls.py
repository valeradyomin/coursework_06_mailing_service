from django.urls import path

from app_mailing.apps import AppMailingConfig

app_name = AppMailingConfig.name

urlpatterns = [
    path('', index, name='home'),
]
