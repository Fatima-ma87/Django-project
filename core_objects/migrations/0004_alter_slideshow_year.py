# Generated by Django 3.2.4 on 2021-08-27 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_objects', '0003_auto_20210827_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='year',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1800, message='Please enter a year between 1850 and 2100'), django.core.validators.MaxValueValidator(2100, message='Please enter a year between 1850 and 2100')], verbose_name='Year'),
        ),
    ]