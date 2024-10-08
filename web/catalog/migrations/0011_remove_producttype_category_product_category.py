# Generated by Django 4.2 on 2024-08-24 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0010_remove_product_types_producttyperelation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="producttype",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="catalog.productcategory"
            ),
        ),
    ]
