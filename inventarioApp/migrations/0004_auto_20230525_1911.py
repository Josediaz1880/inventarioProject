# Generated by Django 3.2.16 on 2023-05-25 23:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0003_auto_20230516_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucionmercancia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entradamercancia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='salidamercancia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]