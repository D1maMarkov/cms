# Generated by Django 4.2 on 2024-05-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0006_alter_featuresblock_introductory_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feature",
            name="icon",
            field=models.ImageField(upload_to="features", verbose_name="Иконка"),
        ),
    ]
