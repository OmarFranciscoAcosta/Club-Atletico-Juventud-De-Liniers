# Generated by Django 4.2.4 on 2023-11-13 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0008_alter_prices_valor_mensual_1semana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='anio',
            field=models.IntegerField(default='2023', verbose_name='Año'),
        ),
    ]