# Generated by Django 4.2.1 on 2023-05-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
