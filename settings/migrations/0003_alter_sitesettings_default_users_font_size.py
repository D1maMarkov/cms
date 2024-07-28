# Generated by Django 4.2 on 2024-07-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0002_sitesettings_default_users_font_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sitesettings",
            name="default_users_font_size",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (6, 6),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (12, 12),
                    (14, 14),
                    (18, 18),
                    (24, 24),
                    (30, 30),
                    (36, 36),
                    (48, 48),
                    (60, 60),
                    (72, 72),
                ],
                null=True,
                verbose_name="Размер пользовательского шрифта по умолчанию",
            ),
        ),
    ]
