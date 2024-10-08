from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from mail.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
