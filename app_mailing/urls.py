from django.urls import path

from app_mailing.apps import AppMailingConfig
from app_mailing.views import index

app_name = AppMailingConfig.name

urlpatterns = [
    path('', index, name='home'),
]
