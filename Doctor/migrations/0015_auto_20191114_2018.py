# Generated by Django 2.2.7 on 2019-11-14 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0014_auto_20191110_0117'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='docotrScheldule',
            new_name='doctorSchedule',
        ),
        migrations.DeleteModel(
            name='TimeSlots',
        ),
    ]