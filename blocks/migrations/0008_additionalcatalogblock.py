# Generated by Django 4.2.7 on 2024-07-06 20:01

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_socialnetwork"),
        ("blocks", "0007_remove_mainpagecatalogblock_add_exclusive_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdditionalCatalogBlock",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="Имя")),
                ("ancor", models.CharField(blank=True, max_length=50, null=True, verbose_name="Якорь")),
                ("title", models.CharField(blank=True, max_length=100, null=True, verbose_name="Заголовок")),
                (
                    "introductory_text",
                    ckeditor.fields.RichTextField(max_length=1000, null=True, verbose_name="Введение"),
                ),
                ("button_text", models.CharField(blank=True, max_length=20, null=True, verbose_name="Текст кнопки")),
                (
                    "block_relation",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="common.blockrelationship"
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blocks.template", verbose_name="html шаблон"
                    ),
                ),
            ],
            options={
                "verbose_name": "Блок каталога на главной",
                "verbose_name_plural": "Блоки каталога на главной",
            },
        ),
    ]