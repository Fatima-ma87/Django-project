# Generated by Django 3.2.4 on 2021-08-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_objects', '0007_auto_20210827_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='previewPicture',
            field=models.ImageField(null=True, upload_to='', verbose_name='Slideshow Picture'),
        ),
    ]