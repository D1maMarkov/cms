# Generated by Django 4.2 on 2024-08-06 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("styles", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="font",
            options={"ordering": ["name"], "verbose_name": "Шрифт", "verbose_name_plural": "Шрифты"},
        ),
    ]
