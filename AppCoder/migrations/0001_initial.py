# Generated by Django 5.0 on 2023-12-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('metodo_de_pago', models.CharField(choices=[('Tarjeta de Credito', 'Tarjeta de Credito'), ('Tarjeta de Debito', 'Tarjeta de Debito'), ('Mercado Pago', 'Mercado Pago'), ('Transferencia', 'Transferencia'), ('Cheque', 'Cheque'), ('Efectivo', 'Efectivo')], default='Tarjeta de Debito', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('comentario', models.TextField()),
            ],
        ),
    ]
