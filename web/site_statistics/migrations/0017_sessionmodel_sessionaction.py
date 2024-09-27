# Generated by Django 5.0 on 2024-09-27 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0016_useractivity_utm_source_alter_useractivity_site"),
    ]

    operations = [
        migrations.CreateModel(
            name="SessionModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("unique_key", models.CharField(max_length=500, null=True, unique=True)),
                ("ip", models.CharField(max_length=15)),
                ("start_time", models.DateTimeField(verbose_name="Дата")),
                ("end_time", models.DateTimeField()),
                ("site", models.CharField(max_length=50, null=True, verbose_name="Сайт")),
                ("device", models.BooleanField(default=False)),
                ("pages_count", models.PositiveIntegerField(default=0, verbose_name="Страницы")),
                ("hacking", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Сессии",
                "verbose_name_plural": "Сессии",
            },
        ),
        migrations.CreateModel(
            name="SessionAction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("adress", models.CharField(max_length=300, verbose_name="страница")),
                ("text", models.CharField(max_length=200, verbose_name="")),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "session",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="site_statistics.sessionmodel"
                    ),
                ),
            ],
            options={
                "verbose_name": "Событие",
                "verbose_name_plural": "События",
                "ordering": ["-id"],
                "abstract": False,
            },
        ),
    ]
