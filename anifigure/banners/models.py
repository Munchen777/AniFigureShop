from django.db import models


def banner_directory_path(instance: "Banner", filename: str):
    return "banners/banner_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Banner(models.Model):
    content = models.FileField(
        default=None,
        upload_to=banner_directory_path,
        verbose_name="Content",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Active",
    )
    start_date = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
        verbose_name="Start Date",
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="End date",
    )

    def __str__(self) -> str:
        return f"Banner {self.pk}"
