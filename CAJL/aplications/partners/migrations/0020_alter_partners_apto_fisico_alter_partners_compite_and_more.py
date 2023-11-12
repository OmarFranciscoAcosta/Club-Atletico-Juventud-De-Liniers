# Generated by Django 4.2.4 on 2023-11-12 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('partners', '0019_alter_partners_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='apto_fisico',
            field=models.BooleanField(default=False, null=True, verbose_name='Apto físico'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='compite',
            field=models.BooleanField(default=False, null=True, verbose_name='Fichado'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='correo',
            field=models.EmailField(blank=True, max_length=40, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='distrito',
            field=models.CharField(blank=True, choices=[('0', 'Provincia de Buenos Aires'), ('1', 'Ciudad Autónoma de Buenos Aires')], max_length=2, null=True, verbose_name='Distrito'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='dni',
            field=models.IntegerField(blank=True, null=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.location'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='socio_activo',
            field=models.BooleanField(default=False, null=True, verbose_name='Socio activo'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='telefono1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono 1'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='telefono2',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono 2'),
        ),
    ]