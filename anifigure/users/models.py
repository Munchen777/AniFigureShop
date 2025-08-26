from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom User model
    
    Attributes:
        email - email of user
        username - username (optional)

    """

    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Email",
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Username",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = (
            "pk",
            "username",
        )
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return self.email or "Anonymous"
