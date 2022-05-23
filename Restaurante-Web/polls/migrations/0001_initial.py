# Generated by Django 4.0.4 on 2022-05-23 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoría')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categpria')),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('precio', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Precio')),
                ('plato', models.CharField(max_length=20, verbose_name='Plato')),
                ('tipo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tipo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.categoria')),
            ],
        ),
    ]