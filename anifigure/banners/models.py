from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from typing import Tuple


class Banner(models.Model):
    BANNER_TYPES: Tuple[str, str] = (
        ("product", "Товар"),
        ("promotion", "Акция"),
        ("advertisement", "Реклама"),
        ("custom", " Пользовательский"),
    )
    POSITIONS: Tuple[str, str] = (
        ("main", "Главная страница"),
        ("category", "Страница категории"),
        ("sidebar", "Боковая панель")
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=200, verbose_name="Подзаголовок")
    banner_type = models.CharField(max_length=50, choices=BANNER_TYPES, verbose_name="Тип баннера")
    position = models.CharField(max_length=50, choices=POSITIONS, verbose_name="Позиция на сайте")
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Тип связанного контента'
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # Медиа файлы
    image = models.ImageField('Изображение', upload_to='banners/', blank=True)

    # Настройки отображения
    is_active = models.BooleanField('Активен', default=True)
    priority = models.IntegerField('Приоритет', default=0)
    start_date = models.DateTimeField('Дата начала показа', null=True, blank=True)
    end_date = models.DateTimeField('Дата окончания показа', null=True, blank=True)
