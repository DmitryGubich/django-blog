from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    bio = models.CharField("basic info", max_length=255, null=True, blank=True)
    avatar = models.ImageField(default="default.png", upload_to="avatars", blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    def __str__(self):
        return self.username
