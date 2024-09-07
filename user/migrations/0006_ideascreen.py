# Generated by Django 4.2 on 2024-09-06 00:49

import django.db.models.deletion
from django.db import migrations, models

import user.models.idea


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_idea_like"),
    ]

    operations = [
        migrations.CreateModel(
            name="IdeaScreen",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("screen", models.ImageField(upload_to=user.models.idea.get_upload_to_idea_screen)),
                ("idea", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="user.idea")),
            ],
        ),
    ]
