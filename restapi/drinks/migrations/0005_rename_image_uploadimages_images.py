# Generated by Django 3.2.14 on 2022-07-22 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_remove_uploadimages_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimages',
            old_name='image',
            new_name='images',
        ),
    ]
