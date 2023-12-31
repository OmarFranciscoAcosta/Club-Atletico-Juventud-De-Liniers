# Generated by Django 4.2.4 on 2023-10-26 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_alter_activities_nombre_actividad_and_more'),
        ('location', '0001_initial'),
        ('partners', '0005_partners_actividades_alter_partners_compite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='actividades',
            field=models.ManyToManyField(to='activities.activities'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='compite',
            field=models.BooleanField(default=False, verbose_name='Fichado'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='distrito',
            field=models.CharField(choices=[('0', 'Provincia de Buenos Aires'), ('1', 'Ciudad Autónoma de Buenos Aires')], max_length=2, verbose_name='Distrito'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='dni',
            field=models.IntegerField(verbose_name='Dni'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.location'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='nombre_completo',
            field=models.CharField(max_length=50, verbose_name='Nombre completo'),
        ),
    ]
