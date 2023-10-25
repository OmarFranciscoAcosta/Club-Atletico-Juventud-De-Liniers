# Generated by Django 4.2.4 on 2023-10-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_alter_prices_mes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prices',
            options={'ordering': ['-anio'], 'verbose_name': 'Precio', 'verbose_name_plural': 'Precios del club'},
        ),
        migrations.AlterField(
            model_name='prices',
            name='anio',
            field=models.IntegerField(verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='mes',
            field=models.CharField(choices=[('0', 'Enero'), ('1', 'Febrero'), ('2', 'Marzo'), ('3', 'Abril'), ('4', 'Mayo'), ('5', 'Junio'), ('6', 'Julio'), ('7', 'Agosto'), ('8', 'Septiembre'), ('9', 'Octubre'), ('10', 'Noviembre'), ('11', 'Diciembre')], default='0', max_length=2, verbose_name='Mes'),
        ),
    ]