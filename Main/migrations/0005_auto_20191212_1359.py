# Generated by Django 2.2.7 on 2019-12-12 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_organdonor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eyedonor',
            old_name='time_f_death',
            new_name='time_of_death',
        ),
    ]