# Generated by Django 4.2 on 2024-04-28 18:15

import colorfield.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("blocks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseColor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Цвет"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Font",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="Имя шрифта")),
                (
                    "link",
                    models.CharField(blank=True, max_length=250, null=True, verbose_name="Ссылка для подключения"),
                ),
            ],
            options={
                "verbose_name": "Шрифт",
                "verbose_name_plural": "Шрифты",
            },
        ),
        migrations.CreateModel(
            name="GlobalStyles",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={
                "verbose_name": "Глобальные стили",
                "verbose_name_plural": "Глобальные стили",
            },
        ),
        migrations.CreateModel(
            name="SubheaderText",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Цвет"
                    ),
                ),
                ("fontWeight", models.CharField(max_length=15, verbose_name="Толщина текста")),
                ("fontWeightMobile", models.CharField(max_length=15, verbose_name="Толщина текста(мобильный)")),
                ("fontSize", models.CharField(blank=True, max_length=15, null=True, verbose_name="Размер текста")),
                ("fontSizeMobile", models.CharField(max_length=15, verbose_name="Размер текста(мобильный)")),
                (
                    "fontColorInverted",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        image_field=None,
                        max_length=25,
                        samples=None,
                        verbose_name="Инвертированный цвет текста",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="styles.font",
                        verbose_name="Шрифт для текста",
                    ),
                ),
                (
                    "global_styles",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="styles.globalstyles"
                    ),
                ),
            ],
            options={
                "verbose_name": "Подзаголовок",
                "verbose_name_plural": "Подзаголовок",
            },
        ),
        migrations.CreateModel(
            name="NavbarCustomStyles",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("margin_top", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ сверху")),
                ("margin_bottom", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ снизу")),
                (
                    "background_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет фона",
                    ),
                ),
                (
                    "photo_darkness",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Затемнение фото в процентах",
                    ),
                ),
                (
                    "header_size",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер заголовка"),
                ),
                (
                    "header_size_mobile",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер заголовка (смартфон)"),
                ),
                (
                    "header_thickness",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина заголовка"),
                ),
                (
                    "header_thickness_mobile",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина заголовка (смартфон)"),
                ),
                (
                    "header_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет заголовка",
                    ),
                ),
                (
                    "main_text_size",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер основного текста"),
                ),
                (
                    "main_text_size_mobile",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="размер основного текста (смартфон)"
                    ),
                ),
                (
                    "main_text_thickness",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина основного текста"),
                ),
                (
                    "main_text_thickness_mobile",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="толщина основного текста (смартфон)"
                    ),
                ),
                (
                    "main_text_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет основного текста",
                    ),
                ),
                (
                    "block",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="blocks.navbar"),
                ),
            ],
            options={
                "verbose_name": "Кастомные стили",
                "verbose_name_plural": "Кастомные стили",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MarginBlock",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("margin_top", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ сверху")),
                ("margin_bottom", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ снизу")),
                (
                    "global_styles",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="styles.globalstyles"
                    ),
                ),
            ],
            options={
                "verbose_name": "Отступы в блоке",
                "verbose_name_plural": "Отступы в блоке",
            },
        ),
        migrations.CreateModel(
            name="MainText",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Цвет"
                    ),
                ),
                ("fontWeight", models.CharField(max_length=15, verbose_name="Толщина текста")),
                ("fontWeightMobile", models.CharField(max_length=15, verbose_name="Толщина текста(мобильный)")),
                ("fontSize", models.CharField(blank=True, max_length=15, null=True, verbose_name="Размер текста")),
                ("fontSizeMobile", models.CharField(max_length=15, verbose_name="Размер текста(мобильный)")),
                (
                    "fontColorInverted",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        image_field=None,
                        max_length=25,
                        samples=None,
                        verbose_name="Инвертированный цвет текста",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="styles.font",
                        verbose_name="Шрифт для текста",
                    ),
                ),
                (
                    "global_styles",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="styles.globalstyles"
                    ),
                ),
            ],
            options={
                "verbose_name": "Основной текст",
                "verbose_name_plural": "Основной текст",
            },
        ),
        migrations.CreateModel(
            name="IconSize",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("height", models.CharField(max_length=20, verbose_name="Высота")),
                ("width", models.CharField(max_length=20, verbose_name="Ширина")),
                (
                    "global_styles",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="styles.globalstyles"
                    ),
                ),
            ],
            options={
                "verbose_name": "Размер иконок",
                "verbose_name_plural": "Размер иконок",
            },
        ),
        migrations.CreateModel(
            name="HeaderText",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Цвет"
                    ),
                ),
                ("fontWeight", models.CharField(max_length=15, verbose_name="Толщина текста")),
                ("fontWeightMobile", models.CharField(max_length=15, verbose_name="Толщина текста(мобильный)")),
                ("fontSize", models.CharField(blank=True, max_length=15, null=True, verbose_name="Размер текста")),
                ("fontSizeMobile", models.CharField(max_length=15, verbose_name="Размер текста(мобильный)")),
                (
                    "fontColorInverted",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        image_field=None,
                        max_length=25,
                        samples=None,
                        verbose_name="Инвертированный цвет текста",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="styles.font",
                        verbose_name="Шрифт для текста",
                    ),
                ),
                (
                    "global_styles",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="styles.globalstyles"
                    ),
                ),
            ],
            options={
                "verbose_name": "Заголовок",
                "verbose_name_plural": "Заголовок",
            },
        ),
        migrations.CreateModel(
            name="ExplanationText",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Цвет"
                    ),
                ),
                ("fontWeight", models.CharField(max_length=15, verbose_name="Толщина текста")),
                ("fontWeightMobile", models.CharField(max_length=15, verbose_name="Толщина текста(мобильный)")),
                ("fontSize", models.CharField(blank=True, max_length=15, null=True, verbose_name="Размер текста")),
                ("fontSizeMobile", models.CharField(max_length=15, verbose_name="Размер текста(мобильный)")),
                (
                    "fontColorInverted",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        image_field=None,
                        max_length=25,
                        samples=None,
                        verbose_name="Инвертированный цвет текста",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="styles.font",
                        verbose_name="Шрифт для текста",
                    ),
                ),
                (
                    "global_styles",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="styles.globalstyles"
                    ),
                ),
            ],
            options={
                "verbose_name": "Текст пояснний",
                "verbose_name_plural": "Текст пояснний",
            },
        ),
        migrations.CreateModel(
            name="CoverCustomStyles",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("margin_top", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ сверху")),
                ("margin_bottom", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ снизу")),
                (
                    "background_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет фона",
                    ),
                ),
                (
                    "photo_darkness",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Затемнение фото в процентах",
                    ),
                ),
                (
                    "header_size",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер заголовка"),
                ),
                (
                    "header_size_mobile",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер заголовка (смартфон)"),
                ),
                (
                    "header_thickness",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина заголовка"),
                ),
                (
                    "header_thickness_mobile",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина заголовка (смартфон)"),
                ),
                (
                    "header_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет заголовка",
                    ),
                ),
                (
                    "main_text_size",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер основного текста"),
                ),
                (
                    "main_text_size_mobile",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="размер основного текста (смартфон)"
                    ),
                ),
                (
                    "main_text_thickness",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина основного текста"),
                ),
                (
                    "main_text_thickness_mobile",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="толщина основного текста (смартфон)"
                    ),
                ),
                (
                    "main_text_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет основного текста",
                    ),
                ),
                (
                    "block",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="blocks.cover"),
                ),
            ],
            options={
                "verbose_name": "Кастомные стили",
                "verbose_name_plural": "Кастомные стили",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ContentCustomStyles",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("margin_top", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ сверху")),
                ("margin_bottom", models.CharField(blank=True, max_length=20, null=True, verbose_name="Отступ снизу")),
                (
                    "background_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет фона",
                    ),
                ),
                (
                    "photo_darkness",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Затемнение фото в процентах",
                    ),
                ),
                (
                    "header_size",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер заголовка"),
                ),
                (
                    "header_size_mobile",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер заголовка (смартфон)"),
                ),
                (
                    "header_thickness",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина заголовка"),
                ),
                (
                    "header_thickness_mobile",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина заголовка (смартфон)"),
                ),
                (
                    "header_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет заголовка",
                    ),
                ),
                (
                    "main_text_size",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="размер основного текста"),
                ),
                (
                    "main_text_size_mobile",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="размер основного текста (смартфон)"
                    ),
                ),
                (
                    "main_text_thickness",
                    models.CharField(blank=True, max_length=50, null=True, verbose_name="толщина основного текста"),
                ),
                (
                    "main_text_thickness_mobile",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="толщина основного текста (смартфон)"
                    ),
                ),
                (
                    "main_text_color",
                    colorfield.fields.ColorField(
                        blank=True,
                        default=None,
                        image_field=None,
                        max_length=25,
                        null=True,
                        samples=None,
                        verbose_name="Цвет основного текста",
                    ),
                ),
                (
                    "block",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="blocks.exampleblock"
                    ),
                ),
            ],
            options={
                "verbose_name": "Кастомные стили",
                "verbose_name_plural": "Кастомные стили",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ColorStyles",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "main_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Основной цвет"
                    ),
                ),
                (
                    "secondary_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Вторичный цвет"
                    ),
                ),
                (
                    "background_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Цвет фона"
                    ),
                ),
                (
                    "second_background_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None, verbose_name="Цвет фона 2"
                    ),
                ),
                (
                    "global_styles",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, to="styles.globalstyles"
                    ),
                ),
            ],
            options={
                "verbose_name": "Цвета",
                "verbose_name_plural": "Цвета",
            },
        ),
    ]
