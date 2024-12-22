# Generated by Django 5.0 on 2024-12-15 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("messanger", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="text",
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="chatuser",
            name="chat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="chat_users", to="messanger.chat"
            ),
        ),
    ]
