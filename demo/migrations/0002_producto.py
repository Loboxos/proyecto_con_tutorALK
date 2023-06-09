# Generated by Django 4.2.1 on 2023-05-05 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),  ##se tiene que ejecutar el primero
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField(default=0)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='demo.marca')),
            ],
        ),
    ]
