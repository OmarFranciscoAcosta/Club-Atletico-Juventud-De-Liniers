# Generated by Django 4.2.4 on 2023-11-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='localidad_nombre',
            field=models.CharField(blank=True, choices=[('0', 'Provincia de Buenos Aires'), ('1', 'Ciudad Autónoma de Buenos Aires')], max_length=1, null=True, verbose_name='Nombre de la localidad'),
        ),
        migrations.AlterField(
            model_name='location',
            name='municipio_nombre',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Nombre del municipio'),
        ),
    ]