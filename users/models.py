from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Phone Number', blank=True, null=True, help_text='Phone number')
    country = models.CharField(max_length=50, verbose_name='Country', blank=True, null=True, help_text='Country')
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Avatar', blank=True, null=True, help_text='Upload your avatar')

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        permissions = [('can_view_user', 'Can view user'), ('can_block_user', 'Can block user')]

    def __str__(self):
        return self.email
