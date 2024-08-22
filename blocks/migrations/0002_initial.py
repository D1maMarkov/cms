# Generated by Django 4.2 on 2024-08-21 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0001_initial"),
        ("catalog", "0001_initial"),
        ("blocks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="catalogproducttype",
            name="product",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="catalog.producttype", verbose_name="Продукт"
            ),
        ),
        migrations.AddField(
            model_name="catalogproduct",
            name="block",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="products", to="blocks.catalogblock"
            ),
        ),
        migrations.AddField(
            model_name="catalogproduct",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="catalog_product",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AddField(
            model_name="catalogblock",
            name="block_relation",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="common.blockrelationship"
            ),
        ),
        migrations.AddField(
            model_name="catalogblock",
            name="product_type",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="catalog.producttype"),
        ),
        migrations.AddField(
            model_name="catalogblock",
            name="template",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blocks.template", verbose_name="html шаблон"
            ),
        ),
        migrations.AddField(
            model_name="block",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="page_block",
                to="common.blockrelationship",
                verbose_name="Блок",
            ),
        ),
        migrations.AddField(
            model_name="block",
            name="page",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blocks",
                to="blocks.page",
                verbose_name="Страница",
            ),
        ),
        migrations.AddField(
            model_name="additionalcatalogproducttype",
            name="block",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="blocks.additionalcatalogblock"),
        ),
        migrations.AddField(
            model_name="additionalcatalogproducttype",
            name="product",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="catalog.producttype", verbose_name="Продукт"
            ),
        ),
        migrations.AddField(
            model_name="additionalcatalogblock",
            name="block_relation",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="common.blockrelationship"
            ),
        ),
        migrations.AddField(
            model_name="additionalcatalogblock",
            name="template",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blocks.template", verbose_name="html шаблон"
            ),
        ),
    ]
