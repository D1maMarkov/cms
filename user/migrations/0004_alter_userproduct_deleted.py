# Generated by Django 4.2 on 2024-09-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_userproduct_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userproduct",
            name="deleted",
            field=models.BooleanField(default=False, verbose_name="Удален"),
        ),
    ]
