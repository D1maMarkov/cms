# Generated by Django 5.0 on 2024-09-27 18:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0017_sessionmodel_sessionaction"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SessionFilters",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("disable_ip", models.BooleanField(verbose_name="Запретить запросы по IP")),
                ("disable_ports", models.BooleanField(verbose_name="Запретить обращение к нетипичным портам")),
                ("disable_robots", models.BooleanField(verbose_name="Разрешить доступ к robots.txt только поисковкам")),
                ("disable_urls", models.TextField(verbose_name="Запрос содержит")),
            ],
            options={
                "verbose_name": "Фильтры сессий",
                "verbose_name_plural": "Фильтры сессий",
            },
        ),
        migrations.AddField(
            model_name="sessionmodel",
            name="auth",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="sessionmodel",
            name="banks_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Банки"),
        ),
        migrations.AddField(
            model_name="sessionmodel",
            name="profile_actions_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Действия в лк"),
        ),
        migrations.AddField(
            model_name="sessionmodel",
            name="user",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="sessionmodel",
            name="utm_source",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="useractivity",
            name="hacking",
            field=models.BooleanField(default=False),
        ),
    ]
