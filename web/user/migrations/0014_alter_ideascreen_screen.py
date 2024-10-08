# Generated by Django 5.0 on 2024-09-19 03:42

from django.db import migrations, models

import infrastructure.files.file_storage
import infrastructure.persistence.models.user.idea


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0013_alter_ideascreen_screen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ideascreen",
            name="screen",
            field=models.ImageField(
                storage=infrastructure.files.file_storage.OverwriteStorage(),
                upload_to=infrastructure.persistence.models.user.idea.get_upload_to_idea_screen,
            ),
        ),
    ]
