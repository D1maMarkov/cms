# Generated by Django 5.0 on 2024-09-08 21:28

import django.db.models.deletion
from django.db import migrations, models

import user.file_storage
import user.models.idea


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0008_idea_admin_answer_alter_idea_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ideascreen",
            name="idea",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="screens", to="user.idea"
            ),
        ),
        migrations.AlterField(
            model_name="ideascreen",
            name="screen",
            field=models.ImageField(
                storage=user.file_storage.OverwriteStorage(), upload_to=user.models.idea.get_upload_to_idea_screen
            ),
        ),
    ]