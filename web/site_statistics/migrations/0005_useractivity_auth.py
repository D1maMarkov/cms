# Generated by Django 5.0 on 2024-09-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0004_useractivity_unique_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="useractivity",
            name="auth",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
