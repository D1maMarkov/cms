# Generated by Django 5.0 on 2024-10-16 22:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0042_sessionfilters_disallowed_host"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionfilters",
            name="hide_admin",
            field=models.BooleanField(default=False),
        ),
    ]