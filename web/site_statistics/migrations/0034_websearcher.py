# Generated by Django 5.0 on 2024-10-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0033_alter_sessionfiltersheader_contain_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebSearcher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ip", models.CharField(max_length=15)),
                ("start_time", models.DateTimeField(verbose_name="Дата")),
                ("end_time", models.DateTimeField()),
                ("site", models.CharField(max_length=50, null=True, verbose_name="Сайт")),
            ],
            options={
                "verbose_name": "Поисковик",
                "verbose_name_plural": "Поисковики",
            },
        ),
    ]