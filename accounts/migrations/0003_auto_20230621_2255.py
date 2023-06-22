# Generated by Django 3.2.16 on 2023-06-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230516_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Permiso',
                'verbose_name_plural': 'Permisos',
            },
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
    ]
