# Generated by Django 4.2 on 2024-05-03 09:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blocks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blockrelationship",
            old_name="block_id",
            new_name="block",
        ),
    ]
