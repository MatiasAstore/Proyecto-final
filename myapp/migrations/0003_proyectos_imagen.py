# Generated by Django 4.2.7 on 2023-11-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mensajecontacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='projectos'),
        ),
    ]