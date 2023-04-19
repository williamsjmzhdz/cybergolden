# Generated by Django 4.2 on 2023-04-19 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('production_cost', models.IntegerField()),
                ('logistics_cost', models.IntegerField()),
                ('photo', models.ImageField(blank=True, default='product-photos/default.png', null=True, upload_to='product-photos')),
                ('stock', models.IntegerField(blank=True, default=0, null=True)),
                ('minimum_stock', models.IntegerField()),
                ('size', models.IntegerField(blank=True, choices=[('0', '0'), ('2', '2'), ('4', '4'), ('6', '6'), ('8', '8'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18'), ('20', '20'), ('34', '34'), ('36', '36'), ('38', '38'), ('40', '40'), ('42', '42'), ('44', '44'), ('46', '46'), ('48', '48'), ('50', '50')], null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
