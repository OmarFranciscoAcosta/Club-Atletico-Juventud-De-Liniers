# Generated by Django 4.2.4 on 2023-10-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_remove_prices_valor_mensual_libre_prices_mes_impago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='mes',
            field=models.CharField(blank=True, choices=[('0', 'Enero'), ('1', 'Febrero'), ('2', 'Marzo'), ('3', 'Abril'), ('4', 'Mayo'), ('5', 'Junio'), ('6', 'Julio'), ('7', 'Agosto'), ('8', 'Septiembre'), ('9', 'Octubre'), ('10', 'Noviembre'), ('11', 'Diciembre')], default='0', max_length=2, verbose_name='Mes'),
        ),
    ]