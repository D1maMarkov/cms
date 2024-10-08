# Generated by Django 4.2 on 2024-08-23 02:54

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_alter_product_annotation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="admin_hint",
            field=ckeditor.fields.RichTextField(blank=True, max_length=1500, null=True, verbose_name="пояснение"),
        ),
        migrations.AlterField(
            model_name="product",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="catalog.organization",
                verbose_name="организация",
            ),
        ),
    ]
