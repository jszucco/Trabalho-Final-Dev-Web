# Generated by Django 3.1.3 on 2020-12-04 14:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promocoes', '0004_auto_20201204_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocao',
            name='favoritos',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]