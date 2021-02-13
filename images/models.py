from django.db import models


class Addimage(models.Model):
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка'
    )
    image_file = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Файл'
    )
