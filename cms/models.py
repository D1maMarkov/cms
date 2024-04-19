from django.core.exceptions import ValidationError
from django.db import models

from utils.errors import Errors

from .validators import validate_html_filename


class Page(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    url = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ["url"]

    def __str__(self):
        return self.title


class BlockRelationship(models.Model):
    block_name = models.CharField(verbose_name="Имя компонента", max_length=50, unique=True)
    block_id = models.PositiveIntegerField()
    
    def __str__(self):
        return self.block_name


class Block(models.Model):
    name = models.ForeignKey(BlockRelationship, verbose_name="Блок", on_delete=models.CASCADE, related_name="page_block")
    page = models.ForeignKey(Page, related_name="blocks", verbose_name="Страница", on_delete=models.CASCADE)

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
        ordering = ["my_order"]

    def __str__(self):
        return str(self.name)


class Template(models.Model):
    name = models.CharField(verbose_name="Название шаблона", max_length=50)
    file = models.CharField(
        verbose_name="Название файла (например base.html)", validators=[validate_html_filename], max_length=50
    )

    class Meta:
        verbose_name = "Html шаблон"
        verbose_name_plural = "Html шаблоны"

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if not validate_html_filename(self.file):
            raise ValidationError({"file": Errors.incorrect_file_name.value})


class BaseBlock(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50, unique=True)
    template = models.ForeignKey(Template, verbose_name="html шаблон", on_delete=models.CASCADE)
    block_relation = models.ForeignKey(BlockRelationship, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        block_relation, _ = BlockRelationship.objects.update_or_create(
            block_name=self.name,
            block_id=self.id
        )

        self.block_relation = block_relation
        super().save(*args, **kwargs)


class ExampleBlock(BaseBlock):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    body = models.TextField(verbose_name="Основной текст", max_length=1000)
    image1 = models.ImageField(verbose_name="Первое изображение", upload_to="images/")
    image2 = models.ImageField(verbose_name="Второе изображение", upload_to="images/")

    class Meta:
        verbose_name = "Контентный блок"
        verbose_name_plural = "Контентные блоки"


class Navbar(BaseBlock):
    title = models.CharField(verbose_name="Заголовок", max_length=100)

    class Meta:
        verbose_name = "навбар"
        verbose_name_plural = "навбар`ы"
