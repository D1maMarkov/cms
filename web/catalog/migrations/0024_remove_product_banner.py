# Generated by Django 5.0 on 2024-09-15 19:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0023_product_banner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="banner",
        ),
    ]
