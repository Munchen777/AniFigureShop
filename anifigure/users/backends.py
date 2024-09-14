from typing import Any
from django.contrib.auth.backends import ModelBackend, get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
from django.http import HttpRequest


UserModel = get_user_model()


class UserModelBackend(ModelBackend):
    """Кастомный бэкенд аутентификации"""

    def authenticate(
        self,
        request: HttpRequest,
        username: str | None = None,
        password: str | None = None,
        **kwargs: Any
    ) -> AbstractBaseUser | None:
        try:
            user = UserModel.objects.get(
                Q(username=username) | Q(email__iexact=username)
            )
        except UserModel.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            return UserModel.objects.filter(email=username).order_by("id").first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
