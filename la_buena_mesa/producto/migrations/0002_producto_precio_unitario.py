# Generated by Django 5.1.3 on 2024-11-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=100),
        ),
    ]
