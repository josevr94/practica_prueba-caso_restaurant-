# Generated by Django 5.1.3 on 2024-11-11 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField()),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('En preparacion', 'En preparacion'), ('Enviado', 'Enviado'), ('Confirmado', 'confirmado')], max_length=20)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('reserva_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reserva.reserva')),
            ],
        ),
    ]
