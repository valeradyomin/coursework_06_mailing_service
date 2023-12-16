from django.urls import path

from app_mailing.apps import AppMailingConfig
from app_mailing.views import MainPage

app_name = AppMailingConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
]
