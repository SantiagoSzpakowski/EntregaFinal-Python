# Generated by Django 4.2 on 2024-09-03 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrincipal', '0002_imagenproyecto_proyecto_delete_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenproyecto',
            name='proyecto',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos', to='AppPrincipal.imagenproyecto'),
        ),
    ]
