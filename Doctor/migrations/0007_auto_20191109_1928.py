# Generated by Django 2.2.7 on 2019-11-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0006_auto_20191109_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docotrscheldule',
            name='closeTime',
            field=models.TimeField(choices=[('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00')]),
        ),
        migrations.AlterField(
            model_name='docotrscheldule',
            name='openTime',
            field=models.TimeField(choices=[('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00')]),
        ),
    ]
