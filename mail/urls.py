from django.urls import path
from mail.apps import MailConfig
from mail.views import home

app_name = MailConfig.name

urlpatterns = [
    path('', home, name='home')
]
