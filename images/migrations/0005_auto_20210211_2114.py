# Generated by Django 3.0.5 on 2021-02-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20210211_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]