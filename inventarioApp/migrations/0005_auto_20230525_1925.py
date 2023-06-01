# Generated by Django 3.2.16 on 2023-05-25 23:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0004_auto_20230525_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entradamercancia',
            options={'verbose_name': 'Entrada mercancía', 'verbose_name_plural': 'Entradas mercancía'},
        ),
        migrations.AlterField(
            model_name='devolucionmercancia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='entradamercancia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='salidamercancia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]