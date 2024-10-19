# Generated by Django 5.0 on 2024-09-20 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_tests", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Error",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("client_ip", models.CharField(max_length=15, verbose_name="ip с которого был запрос")),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="время")),
                ("status", models.SmallIntegerField(null=True, verbose_name="статус")),
                ("message", models.TextField(max_length=10000, verbose_name="сообщение об ошибке")),
                ("path", models.CharField(max_length=200, verbose_name="страница")),
                (
                    "user",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]