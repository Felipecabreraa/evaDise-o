# Generated by Django 4.2.5 on 2023-11-28 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0009_alter_prestamo_fecha_prestamo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='usuario',
            new_name='usuario_solicitante',
        ),
    ]
