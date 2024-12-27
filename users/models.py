from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='имя пользователя', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
