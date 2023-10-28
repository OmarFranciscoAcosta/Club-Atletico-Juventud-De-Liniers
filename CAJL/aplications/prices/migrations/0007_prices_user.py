# Generated by Django 4.2.4 on 2023-10-28 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prices', '0006_prices_medio_mes_prices_valor_patin3semanaescula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prices',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]