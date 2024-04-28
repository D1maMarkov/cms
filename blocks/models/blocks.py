from ckeditor.fields import RichTextField
from django.db import models

from .common import BaseBlock, ButtonMixin


class ExampleBlock(BaseBlock, ButtonMixin):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    body = RichTextField(verbose_name="Основной текст", max_length=1000)
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


class Cover(BaseBlock, ButtonMixin):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = RichTextField(verbose_name="Основной текст", max_length=500)
    image_desctop = models.ImageField(verbose_name="Картинка(десктоп)", upload_to="images/covers/")
    image_mobile = models.ImageField(verbose_name="Картинка(смартфон)", upload_to="images/covers/")
    second_button_text = models.CharField(verbose_name="Текст второй кнопки", max_length=20)
    second_button_ref = models.CharField(verbose_name="Ссылка для второй кнопки", max_length=20)

    class Meta:
        verbose_name = "Обложка"
        verbose_name_plural = "Обложки"