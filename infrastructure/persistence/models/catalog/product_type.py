from ckeditor.fields import RichTextField
from django.db import models

from infrastructure.persistence.models.blocks.blocks import Cover


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    short = models.CharField(max_length=100, verbose_name="Сокращение", null=True)

    class Meta:
        app_label = "catalog"
        verbose_name = "Категория продуктов"
        verbose_name_plural = "Категории продуктов"

    def __str__(self):
        return self.name


class ProductType(models.Model):
    PRODUCT_TYPE_STATUSES = (("Опубликовано", "Опубликовано"), ("Скрыто", "Скрыто"))

    status = models.CharField(verbose_name="статус", choices=PRODUCT_TYPE_STATUSES, null=True, max_length=100)
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    image = models.ImageField(upload_to="organizations/covers", verbose_name="Этикетка", null=True)

    cover = models.ForeignKey(Cover, on_delete=models.SET_NULL, null=True, verbose_name="блок обложки")
    description = RichTextField(max_length=1000, verbose_name="Аннотация")

    profit = models.CharField(max_length=500, verbose_name="Выгода", null=True)

    class Meta:
        app_label = "catalog"
        verbose_name = "Тип продукта/акции"
        verbose_name_plural = "Типы продукта/акции"

    def __str__(self):
        return self.name
