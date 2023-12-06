# Generated by Django 4.2 on 2023-12-06 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_inventory_created_at_inventory_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
