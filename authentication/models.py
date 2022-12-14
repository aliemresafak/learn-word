from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name=_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.get_full_name()
