# Generated by Django 4.2.7 on 2024-06-04 15:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_alter_producttype_cover"),
    ]

    operations = [
        migrations.RenameField(
            model_name="producttype",
            old_name="cover",
            new_name="image",
        ),
    ]