# Generated by Django 4.2 on 2024-08-21 18:19

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0002_domain_font_globalstyles_socialnetwork_userfont_and_more"),
        ("user", "0005_user_user_user_sponsor_9e3e2d_idx"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="register_on_domain",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="register_on_domain",
                to="settings.domain",
                verbose_name="зарегистрирован на домене",
            ),
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("subdomain", models.CharField(max_length=50, unique=True, verbose_name="поддомен")),
                ("logo", models.ImageField(blank=True, null=True, upload_to="images/logo", verbose_name="Лого")),
                ("logo_width", models.CharField(blank=True, max_length=20, null=True, verbose_name="ширина лого")),
                (
                    "logo_width_mobile",
                    models.CharField(blank=True, max_length=20, null=True, verbose_name="ширина лого(мобильный)"),
                ),
                (
                    "logo2",
                    models.ImageField(blank=True, null=True, upload_to="images/logo", verbose_name="Лого для форм"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="активный")),
                (
                    "use_default_settings",
                    models.BooleanField(default=False, verbose_name="Использовать общие настройки сайта"),
                ),
                ("advertising_channel", models.CharField(max_length=100, null=True, verbose_name="Рекламный канал")),
                (
                    "online_from",
                    models.DateField(
                        default=datetime.datetime(2024, 8, 21, 18, 19, 36, 708428, tzinfo=datetime.timezone.utc),
                        verbose_name="онлайн с",
                    ),
                ),
                ("name", models.CharField(max_length=50, null=True, verbose_name="Название сайта")),
                ("font_size", models.PositiveIntegerField(null=True, verbose_name="размер шрифта")),
                ("owner", models.CharField(max_length=150, null=True, verbose_name="Владелец")),
                ("contact_info", models.CharField(max_length=200, null=True, verbose_name="Контактная информация")),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True, verbose_name="сайт создан")),
                (
                    "domain",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="settings.domain",
                        verbose_name="домен",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="settings.userfont",
                        verbose_name="шрифт",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="site",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "сайт",
                "verbose_name_plural": "сайты",
                "db_table": "domens_site",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="register_on_site",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="register_on_site",
                to="user.site",
                verbose_name="зарегистрирован на сайте",
            ),
        ),
    ]
