# Generated by Django 4.2 on 2023-04-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_delete_comprador_delete_vendedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculo',
            old_name='kilometraje',
            new_name='anio',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(max_length=50),
        ),
    ]
