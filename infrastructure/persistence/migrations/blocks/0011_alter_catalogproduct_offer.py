# Generated by Django 5.0 on 2024-09-10 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0010_alter_catalogproduct_offer"),
        ("catalog", "0021_offer_link_alter_offertyperelation_offer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalogproduct",
            name="offer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="catalog_product",
                to="catalog.offer",
                verbose_name="Оффер",
            ),
        ),
    ]