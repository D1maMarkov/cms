# Generated by Django 4.2 on 2024-08-25 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0011_remove_producttype_category_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.productcategory",
                verbose_name="категория",
            ),
        ),
    ]
