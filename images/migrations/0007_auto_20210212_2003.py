# Generated by Django 3.0.5 on 2021-02-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20210211_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]