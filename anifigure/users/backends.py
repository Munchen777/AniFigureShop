from django.contrib.auth.backends import ModelBackend, get_user_model
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q


class UserModelBackend(ModelBackend):
    """
    Переопределение аутентификации

    Выполняем аутентификацию по никнэйму или по почте.
    Если пользователя не существует возвращаем None.
    Если найдено несколько пользователей, возвращаем,
    выполнив фильтрацию по email

    """

    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(Q(email=username or email) | Q(email=email))
        except UserModel.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            return UserModel.objects.filter(email=email).order_by("pk").first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
