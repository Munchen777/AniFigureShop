from django.db import models
from django.contrib.auth.models import AbstractUser


from users.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self) -> str:
        return self.username or "no name"
