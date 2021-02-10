from django.db import models


class Image(models.Model):
    image_url = models.URLField(
        blank=True, verbose_name='Ссылка'
    )
    image_file = models.ImageField(
        upload_to='images/', blank=True, verbose_name='Файл'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('image_url', 'image_file'), name='unique'
            )
        ]

    def __str__(self):
        return str(self.pk)
