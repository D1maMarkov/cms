# Generated by Django 4.2.7 on 2024-06-23 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0001_initial"),
        ("blocks", "0003_delete_promocatalog"),
    ]

    operations = [
        migrations.CreateModel(
            name="PromoCatalog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="Имя")),
                ("ancor", models.CharField(blank=True, max_length=50, null=True, verbose_name="Якорь")),
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
                "verbose_name": "Промо акции",
                "verbose_name_plural": "Промо акциий",
            },
        ),
    ]
