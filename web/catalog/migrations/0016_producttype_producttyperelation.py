# Generated by Django 5.0 on 2024-09-09 20:57

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0005_remove_additionalcatalogproducttype_offer_and_more"),
        ("catalog", "0015_delete_producttype_delete_producttyperelation"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.CharField(
                        choices=[("Опубликовано", "Опубликовано"), ("Скрыто", "Скрыто")],
                        max_length=100,
                        null=True,
                        verbose_name="статус",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Название")),
                ("slug", models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name="URL")),
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                ("image", models.ImageField(null=True, upload_to="organizations/covers", verbose_name="Этикетка")),
                ("description", ckeditor.fields.RichTextField(max_length=1000, verbose_name="Аннотация")),
                (
                    "cover",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blocks.cover",
                        verbose_name="блок обложки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип продукта/акции",
                "verbose_name_plural": "Типы продукта/акции",
            },
        ),
        migrations.CreateModel(
            name="ProductTypeRelation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("profit", models.CharField(max_length=500, verbose_name="Выгода")),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="types",
                        to="catalog.product",
                        verbose_name="Тип продукта",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.producttype",
                        verbose_name="продукт",
                    ),
                ),
            ],
        ),
    ]