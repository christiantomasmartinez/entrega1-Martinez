# Generated by Django 4.2 on 2023-04-26 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_queja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queja',
            name='anonima',
        ),
        migrations.RemoveField(
            model_name='queja',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='queja',
            name='usuario',
        ),
    ]
