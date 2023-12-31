# Generated by Django 4.2.5 on 2023-11-27 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_libro_autor_libro_año_publicacion_libro_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('fecha_devolucion_estimada', models.DateField()),
                ('fecha_devolucion_real', models.DateField(blank=True, null=True)),
                ('dias_retraso', models.IntegerField(default=0)),
                ('multa', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('costo_prestamo', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('libros', models.ManyToManyField(to='biblioteca.libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.usuario')),
            ],
        ),
    ]
