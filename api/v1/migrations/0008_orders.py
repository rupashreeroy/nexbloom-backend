# Generated by Django 4.2 on 2024-10-20 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0007_category_image_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.FloatField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_order', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.products')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
