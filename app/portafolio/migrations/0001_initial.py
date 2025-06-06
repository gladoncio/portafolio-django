# Generated by Django 5.2.2 on 2025-06-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('icono_svg', models.TextField(blank=True, null=True)),
                ('icono_imagen', models.ImageField(blank=True, null=True, upload_to='tecnologias/')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('enlace', models.URLField(blank=True, null=True)),
                ('tecnologias', models.ManyToManyField(to='portafolio.tecnologia')),
            ],
        ),
    ]
