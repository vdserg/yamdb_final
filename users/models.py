from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', _('user')
        MODERATOR = 'moderator', _('moderator')
        ADMIN = 'admin', _('admin')

    email = models.EmailField(max_length=30, unique=True)
    bio = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=9, choices=Role.choices,
                            default=Role.USER)
    auth_code = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=15, blank=True)

    REQUIRED_FIELDS = ('username',)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
