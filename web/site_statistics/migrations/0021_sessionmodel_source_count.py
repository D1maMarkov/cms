# Generated by Django 5.0 on 2024-09-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0020_sessionmodel_hacking_reason_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionmodel",
            name="source_count",
            field=models.PositiveIntegerField(default=0, verbose_name="ресурсы"),
        ),
    ]
