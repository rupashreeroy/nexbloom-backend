# Generated by Django 4.2 on 2024-10-10 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_products_brand_name_alter_brands_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productimages',
            table='products_images',
        ),
    ]
