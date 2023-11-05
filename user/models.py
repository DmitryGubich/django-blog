from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import UserManager


class User(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
