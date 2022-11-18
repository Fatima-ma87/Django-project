# Generated by Django 3.2.4 on 2021-08-27 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_objects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='date',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1850, message='Please enter a year between 1850 and 2021'), django.core.validators.MaxValueValidator(2060, message='Please enter a year between 1850 and 2060')], verbose_name='Year'),
        ),
    ]
