# Generated by Django 4.2 on 2024-08-02 19:42

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0001_initial"),
        ("blocks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CatalogPageTemplate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=50, verbose_name="Заголовок")),
            ],
            options={
                "verbose_name": "каталог",
                "verbose_name_plural": "каталог",
            },
        ),
        migrations.CreateModel(
            name="ExclusiveCard",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("button_text", models.CharField(blank=True, max_length=20, null=True, verbose_name="Текст кнопки")),
                (
                    "button_ref",
                    models.CharField(blank=True, max_length=20, null=True, verbose_name="Ссылка для кнопки"),
                ),
                ("image", models.ImageField(upload_to="images/exclusive", verbose_name="картинка")),
                ("bonus", models.CharField(max_length=50, verbose_name="бонус")),
                ("annotation", models.TextField(max_length=700, null=True, verbose_name="аннотация")),
            ],
            options={
                "verbose_name": "Карточка Эксклюзив",
                "verbose_name_plural": "Карточка Эксклюзив",
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("logo", models.ImageField(upload_to="organizations/logos/", verbose_name="Лого")),
                ("site", models.URLField(max_length=500, verbose_name="сайт")),
                ("admin_hint", ckeditor.fields.RichTextField(max_length=1500, verbose_name="пояснение для админа")),
            ],
            options={
                "verbose_name": "Организация",
                "verbose_name_plural": "Организации",
            },
        ),
        migrations.CreateModel(
            name="OrganizationType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Тип организации",
                "verbose_name_plural": "Типы организаций",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Название")),
                ("slug", models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name="URL")),
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                ("image", models.ImageField(null=True, upload_to="organizations/covers", verbose_name="Этикетка")),
                ("description", ckeditor.fields.RichTextField(max_length=1000, verbose_name="Аннотация")),
                ("profit", models.CharField(max_length=500, verbose_name="Выгода")),
                (
                    "cover",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blocks.cover",
                        verbose_name="блок обложки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип продукта/акции",
                "verbose_name_plural": "Типы продукта/акции",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cover", models.ImageField(upload_to="products/covers", verbose_name="Обложка")),
                ("name", models.CharField(max_length=100, verbose_name="Название продукта")),
                ("annotation", models.CharField(max_length=300, verbose_name="Аннотация")),
                ("description", ckeditor.fields.RichTextField(max_length=5000, verbose_name="Описание")),
                (
                    "banner",
                    models.ImageField(blank=True, null=True, upload_to="products/banners/", verbose_name="Баннер"),
                ),
                ("promote", models.DateField(blank=True, null=True, verbose_name="Продвигать до")),
                (
                    "private",
                    models.BooleanField(verbose_name="Приватный(виден только зарегистрированным пользователям)"),
                ),
                ("promotion", models.BooleanField(verbose_name="Акция")),
                ("profit", models.CharField(help_text="₽", max_length=500, verbose_name="Выгода")),
                ("start_promotion", models.DateField(blank=True, null=True, verbose_name="Начало акции")),
                ("end_promotion", models.DateField(blank=True, null=True, verbose_name="Окончание акции")),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("Новое", "Новое"), ("Опубликовано", "Опубликовано")],
                        default="Новое",
                        max_length=50,
                        verbose_name="статус",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.organization",
                        verbose_name="организация",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.producttype",
                        verbose_name="Тип продукта",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт/акция",
                "verbose_name_plural": "продукты/акции",
                "ordering": ["end_promotion"],
            },
        ),
        migrations.AddField(
            model_name="organization",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="catalog.organizationtype", verbose_name="Тип"
            ),
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.URLField(max_length=300, verbose_name="ссылка")),
                (
                    "percent",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="процент",
                    ),
                ),
                ("info", models.CharField(blank=True, max_length=300, null=True, verbose_name="Инфо")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="links", to="catalog.product"
                    ),
                ),
            ],
            options={
                "verbose_name": "ссылки",
            },
        ),
        migrations.CreateModel(
            name="Block",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("my_order", models.PositiveIntegerField(default=0)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="catalog_block",
                        to="common.blockrelationship",
                        verbose_name="Блок",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blocks",
                        to="catalog.catalogpagetemplate",
                        verbose_name="Страница",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блок",
                "verbose_name_plural": "Блоки",
                "ordering": ["my_order"],
                "abstract": False,
            },
        ),
    ]
