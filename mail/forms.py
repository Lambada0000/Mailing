from django.forms import ModelForm, BooleanField

from mail.models import Newsletter, Message, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class NewsletterForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        exclude = ('owner',)


class NewsletterModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        fields = ('is_active', 'owner',)


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)
