# Generated by Django 4.2.4 on 2023-11-09 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0016_rename_fecha_emision_apto_fisico_partners_fecha_emisión_apto_fisico_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partners',
            old_name='fecha_emisión_apto_fisico',
            new_name='fecha_emisión_apto_físico',
        ),
    ]
