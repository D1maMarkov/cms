# Generated by Django 5.0 on 2024-10-11 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_statistics", "0025_sessionmodel_bun_rate_alter_useraction_session"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sessionfilters",
            old_name="disable_ports",
            new_name="ports_penalty",
        ),
        migrations.RemoveField(
            model_name="sessionfilters",
            name="disable_ip",
        ),
        migrations.RemoveField(
            model_name="sessionfilters",
            name="disable_robots",
        ),
        migrations.AddField(
            model_name="sessionfilters",
            name="ban_limit",
            field=models.SmallIntegerField(default=0, verbose_name="Порог бана"),
        ),
        migrations.AddField(
            model_name="sessionfilters",
            name="capcha_error",
            field=models.SmallIntegerField(default=0, verbose_name="Ошибка в капче"),
        ),
        migrations.AddField(
            model_name="sessionfilters",
            name="capcha_limit",
            field=models.SmallIntegerField(default=0, verbose_name="Порог капчи"),
        ),
        migrations.AddField(
            model_name="sessionfilters",
            name="ip_penalty",
            field=models.SmallIntegerField(default=0, verbose_name="Порог бана"),
        ),
        migrations.AddField(
            model_name="sessionfilters",
            name="reject_capcha",
            field=models.SmallIntegerField(default=0, verbose_name="Отказ от капчи"),
        ),
        migrations.AddField(
            model_name="sessionfilters",
            name="searchers",
            field=models.TextField(null=True, verbose_name="Поисковики"),
        ),
        migrations.CreateModel(
            name="SessionFiltersHeader",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("header", models.CharField(max_length=50, verbose_name="Заголовок")),
                (
                    "contain",
                    models.CharField(
                        choices=[
                            ("Присутствует", "Присутствует"),
                            ("Отсутствует", "Отсутствует"),
                            ("Содержит", "Содержит"),
                            ("Не содержит", "Не содержит"),
                            ("Совпадает", "Совпадает"),
                            ("Не совпадает", "Не совпадает"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "session_filters",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="site_statistics.sessionfilters"),
                ),
            ],
        ),
    ]