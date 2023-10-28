# Generated by Django 4.2.4 on 2023-10-28 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0002_payments_anio_payments_mes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payments',
            name='anio',
            field=models.IntegerField(verbose_name='Año'),
        ),
    ]
