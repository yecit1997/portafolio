# Generated by Django 5.1.5 on 2025-04-17 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_alter_proyectos_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('icono', models.ImageField(upload_to='redes')),
            ],
            options={
                'verbose_name': 'Red',
                'verbose_name_plural': 'Redes',
            },
        ),
        migrations.CreateModel(
            name='ImagenProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='galeria_proyectos')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Texto Alternativo')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_proyecto', to='portafolio.proyectos')),
            ],
            options={
                'verbose_name': 'Imagen del Proyecto',
                'verbose_name_plural': 'Imágenes del Proyecto',
            },
        ),
        migrations.CreateModel(
            name='SobreMi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='sobre_mi')),
                ('redes', models.ManyToManyField(blank=True, related_name='redes', to='portafolio.redes')),
            ],
            options={
                'verbose_name': 'Sobre_mi',
                'verbose_name_plural': 'Sobre_mi',
            },
        ),
    ]
