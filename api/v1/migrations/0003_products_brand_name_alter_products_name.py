# Generated by Django 4.2 on 2024-10-10 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_category_products_productimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
