# Generated by Django 4.2.7 on 2024-06-08 13:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0009_product_created_at_product_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="status",
        ),
    ]
