# Generated by Django 4.2.7 on 2024-07-06 21:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0009_additionalcatalogproducttype"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="additionalcatalogblock",
            options={"verbose_name": "Дополнительный каталог", "verbose_name_plural": "Дополнительные каталоги"},
        ),
        migrations.RemoveField(
            model_name="additionalcatalogblock",
            name="introductory_text",
        ),
        migrations.RemoveField(
            model_name="additionalcatalogblock",
            name="title",
        ),
    ]