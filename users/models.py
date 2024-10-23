from django.contrib.auth.models import AbstractUser
from django.db import models

OPTIONAL = {'blank': True, 'null': True}

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=35, verbose_name='Номер телефона', **OPTIONAL)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', verbose_name='Аватар', **OPTIONAL)
    location = models.CharField(max_length=100, verbose_name='Местоположение', **OPTIONAL)
    telegram_chat_id = models.CharField(max_length=100, verbose_name='Telegram Chat ID', **OPTIONAL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def str(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'