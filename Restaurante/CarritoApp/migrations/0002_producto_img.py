# Generated by Django 4.0.4 on 2022-07-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarritoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.ImageField(null=True, upload_to='Polls/static/Polls/img/', verbose_name='Imagen'),
        ),
    ]
