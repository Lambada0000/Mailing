from django.urls import path
from mail.apps import MailConfig
from mail.views import home, NewsletterDeleteView, MessageCreateView, MessageListView, MessageDetailView, \
    MessageUpdateView, MessageDeleteView, ClientListView, ClientDetailView, ClientUpdateView, ClientCreateView, \
    ClientDeleteView, AttemptListView
from mail.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView

app_name = MailConfig.name

urlpatterns = [
    path('', home, name='home'),

    # Рассылки
    path('newsletter/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/<int:pk>/update', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/<int:pk>/delete/', NewsletterDeleteView.as_view(), name='newsletter_delete'),

    # Попытка рассылки
    path('attempts/', AttemptListView.as_view(), name='attempt_list'),

    # Сообщения
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/<int:pk>/update', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    # Клиенты
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name='client_update'),
]
