from django.forms import ModelForm

from mail.models import Newsletter, Message, Client


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        exclude = ('owner',)


class NewsletterModeratorForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ('is_active', 'owner',)


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)


class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)
