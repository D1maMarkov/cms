from ckeditor.fields import RichTextField
from django.db import models


class Document(models.Model):
    image = models.ImageField(upload_to="docs", verbose_name="Обложка")
    title = models.CharField(max_length=300, verbose_name="Название")
    text = RichTextField(max_length=300000, verbose_name="Содержание")
    name = models.CharField(max_length=300, verbose_name="Загаловок", null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        app_label = "materials"
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title
