# Generated by Django 5.0 on 2024-09-16 21:16

from django.db import migrations, models

import infrastructure.files.file_storage
import infrastructure.persistence.models.user.idea


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0012_alter_roles_options"),
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