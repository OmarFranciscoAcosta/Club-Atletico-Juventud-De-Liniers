# Generated by Django 4.2.5 on 2023-11-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_payments_user_alter_payments_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='anio',
            field=models.IntegerField(blank=True, verbose_name='Año facturado'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='mes',
            field=models.CharField(blank=True, choices=[('0', 'Enero'), ('1', 'Febrero'), ('2', 'Marzo'), ('3', 'Abril'), ('4', 'Mayo'), ('5', 'Junio'), ('6', 'Julio'), ('7', 'Agosto'), ('8', 'Septiembre'), ('9', 'Octubre'), ('10', 'Noviembre'), ('11', 'Diciembre')], max_length=2, verbose_name='Mes facturado'),
        ),
    ]
