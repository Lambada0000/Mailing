from django.contrib import admin

from mail.models import Client, Newsletter, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment')
    list_filter = ('email', 'name')
    search_fields = ('email', 'name')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'frequency', 'status', 'message')
    search_fields = ('name', 'clients')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'text')
    search_fields = ('subject',)
