# Generated by Django 4.0.5 on 2022-08-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0002_alter_mensaje_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='contenido',
            field=models.TextField(),
        ),
    ]
