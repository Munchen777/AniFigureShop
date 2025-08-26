from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_field):
        if not email:
            raise ValueError(_("The Email field must be set"))

        email = self.normalize_email(email=email)
        user = self.model(email=email, username=username, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)
        extra_field.setdefault("is_active", True)

        if extra_field.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_field.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email=email, password=password, **extra_field)
