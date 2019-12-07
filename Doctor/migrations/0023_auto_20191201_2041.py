# Generated by Django 2.2.7 on 2019-12-01 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Doctor', '0022_auto_20191116_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicaddress',
            name='Address_ID',
        ),
        migrations.RemoveField(
            model_name='clinicaddress',
            name='Doctor_ID',
        ),
        migrations.AddField(
            model_name='clinicaddress',
            name='ClinicAddress_ID',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='clinicaddress',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Doctor_Address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Doctor.ClinicAddress'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Doctor_License',
            field=models.CharField(default='1234567890', max_length=25, null=True),
        ),
    ]