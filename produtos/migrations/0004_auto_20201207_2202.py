# Generated by Django 3.1.4 on 2020-12-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_auto_20201204_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]