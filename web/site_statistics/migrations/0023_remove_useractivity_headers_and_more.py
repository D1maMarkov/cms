# Generated by Django 5.0 on 2024-09-30 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0022_sessionmodel_headers_useractivity_headers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useractivity",
            name="headers",
        ),
        migrations.AlterField(
            model_name="sessionaction",
            name="session",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actions",
                to="site_statistics.sessionmodel",
            ),
        ),
    ]
