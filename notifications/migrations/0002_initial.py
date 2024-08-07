# Generated by Django 4.2 on 2024-08-02 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usernotification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="пользователь"
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="trigger",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="notifications.trigger",
                verbose_name="триггер",
            ),
        ),
    ]
