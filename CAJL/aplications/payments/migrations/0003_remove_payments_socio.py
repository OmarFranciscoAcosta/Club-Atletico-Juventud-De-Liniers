# Generated by Django 4.2.4 on 2023-10-25 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_payments_options_payments_socio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='socio',
        ),
    ]
