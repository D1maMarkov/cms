# Generated by Django 5.0 on 2024-10-12 22:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0028_sessionfilters_disable_urls_penalty_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sessionmodel",
            old_name="bun_rate",
            new_name="ban_rate",
        ),
    ]
