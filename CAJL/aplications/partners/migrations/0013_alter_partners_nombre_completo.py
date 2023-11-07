# Generated by Django 4.2.4 on 2023-11-07 02:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0012_alter_partners_telefono1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='nombre_completo',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Este campo solo puede contener letras y espacios en blanco.', regex='^[a-zA-Z\\s]*$')], verbose_name='Nombre completo'),
        ),
    ]
