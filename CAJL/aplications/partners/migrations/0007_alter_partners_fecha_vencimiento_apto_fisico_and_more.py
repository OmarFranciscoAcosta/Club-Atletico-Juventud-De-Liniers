# Generated by Django 4.2.4 on 2023-10-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0006_alter_partners_actividades_alter_partners_compite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='fecha_vencimiento_apto_fisico',
            field=models.DateField(blank=True, verbose_name='Fecha de emisión del apto físico'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='fecha_vencimiento_fichaje',
            field=models.DateField(blank=True, verbose_name='Fecha de emisión del fichaje'),
        ),
    ]
