# Generated by Django 3.2.4 on 2021-08-27 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_objects', '0002_alter_slideshow_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slideshow',
            old_name='date',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='slideshow',
            name='title',
        ),
    ]
