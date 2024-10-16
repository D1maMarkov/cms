# Generated by Django 5.0 on 2024-10-11 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0024_alter_sessionaction_options_alter_useraction_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionmodel",
            name="bun_rate",
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="useraction",
            name="session",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actions",
                to="site_statistics.useractivity",
            ),
        ),
    ]
