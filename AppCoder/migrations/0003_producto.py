# Generated by Django 5.0 on 2023-12-12 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.empleado')),
            ],
        ),
    ]
