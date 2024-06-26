# Generated by Django 4.2.7 on 2024-06-21 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "disable_partners_sites",
                    models.BooleanField(default=False, verbose_name="Отключить партнёрский домен"),
                ),
            ],
            options={
                "verbose_name": "Настройки сайта",
                "verbose_name_plural": "Настройки сайта",
            },
        ),
        migrations.CreateModel(
            name="Logo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="images/logo", verbose_name="Изображение")),
                ("width", models.CharField(max_length=20, verbose_name="Ширина")),
                ("height", models.CharField(max_length=20, verbose_name="Высота")),
                ("width_mobile", models.CharField(max_length=20, verbose_name="Ширина(смартфон)")),
                ("height_mobile", models.CharField(max_length=20, verbose_name="Высота(смартфон)")),
                (
                    "settings",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="logo", to="settings.sitesettings"
                    ),
                ),
            ],
            options={
                "verbose_name": "Логотип",
                "verbose_name_plural": "Логотип",
            },
        ),
        migrations.CreateModel(
            name="Icon",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="images/icon", verbose_name="Изображение")),
                (
                    "settings",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="icon", to="settings.sitesettings"
                    ),
                ),
            ],
            options={
                "verbose_name": "Иконка",
                "verbose_name_plural": "Иконка",
            },
        ),
        migrations.CreateModel(
            name="FormLogo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="images/logo", verbose_name="Изображение")),
                ("width", models.CharField(max_length=20, verbose_name="Ширина")),
                ("height", models.CharField(max_length=20, verbose_name="Высота")),
                ("width_mobile", models.CharField(max_length=20, verbose_name="Ширина(смартфон)")),
                ("height_mobile", models.CharField(max_length=20, verbose_name="Высота(смартфон)")),
                (
                    "settings",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="form_logo",
                        to="settings.sitesettings",
                    ),
                ),
            ],
            options={
                "verbose_name": "Логотип для форм",
                "verbose_name_plural": "Логотип для форм",
            },
        ),
    ]
