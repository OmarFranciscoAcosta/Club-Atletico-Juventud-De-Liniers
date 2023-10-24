# Generated by Django 4.2.4 on 2023-10-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_remove_activities_modified_by'),
        ('partners', '0004_alter_partners_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='actividades',
            field=models.ManyToManyField(blank=True, to='activities.activities'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='compite',
            field=models.BooleanField(default=False, verbose_name='Fichado?'),
        ),
    ]
