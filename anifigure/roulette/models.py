from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
# Модель которая добавляет юзеру попытки кручения рулетки
class SpinAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attempts = models.PositiveIntegerField(default=1)  # Количество доступных попыток

    def __str__(self):
        return f"{self.user.username} - {self.attempts} попыток"


# Создает попытку кручения рулетки при регистрации пользователя
@receiver(post_save, sender=User)
def create_spin_attempt(sender, instance, created, **kwargs):
    if created:
        SpinAttempt.objects.create(user=instance)
