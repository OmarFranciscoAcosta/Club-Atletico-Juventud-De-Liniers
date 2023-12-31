# Generated by Django 4.2.5 on 2023-11-10 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('partners', '0017_rename_fecha_emisión_apto_fisico_partners_fecha_emisión_apto_físico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='distrito',
            field=models.CharField(blank=True, choices=[('0', 'Provincia de Buenos Aires'), ('1', 'Ciudad Autónoma de Buenos Aires')], max_length=2, verbose_name='Distrito'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='localidad',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.location'),
        ),
    ]
