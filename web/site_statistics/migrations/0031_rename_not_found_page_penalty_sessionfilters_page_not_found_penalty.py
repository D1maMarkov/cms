# Generated by Django 5.0 on 2024-10-13 01:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0030_sessionfilters_not_found_page_penalty_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sessionfilters",
            old_name="not_found_page_penalty",
            new_name="page_not_found_penalty",
        ),
    ]
