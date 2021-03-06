# Generated by Django 3.0.5 on 2021-02-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, height_field='image_height', upload_to='images/', verbose_name='Файл', width_field='image_width'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_height',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_width',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Ширина'),
        ),
    ]
