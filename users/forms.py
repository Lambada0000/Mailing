from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
