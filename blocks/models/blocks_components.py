from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.db import models

from .blocks import FeaturesBlock, Navbar, QuestionsBlock, SocialMediaBlock
from .mixins import ButtonMixin, TitleMixin


class NavMenuItem(ButtonMixin):
    navbar = models.ForeignKey(Navbar, on_delete=models.SET_NULL, null=True, related_name="menu_items")


class Feature(TitleMixin):
    icon = models.ImageField(verbose_name="Иконка", upload_to="images/features")
    description = models.TextField(verbose_name="Пояснение")
    block = models.ForeignKey(
        FeaturesBlock, verbose_name="Блок", on_delete=models.SET_NULL, null=True, related_name="features"
    )

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        try:
            this = Feature.objects.get(id=self.id)
            if this.icon != self.icon:
                this.icon.delete()
        except:
            pass
        super().save(*args, **kwargs)


class SocialMediaButton(models.Model):
    icon = models.ImageField(verbose_name="Изображение", upload_to="images/social")
    background_color = ColorField(verbose_name="Цвет фона")
    ref = models.CharField(verbose_name="Ссылка на соц. сети", max_length=500)
    text = models.CharField(verbose_name="Текст", max_length=100, null=True)

    block = models.ForeignKey(SocialMediaBlock, on_delete=models.CASCADE, related_name="buttons")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


class Question(TitleMixin):
    text = RichTextField(verbose_name="текст вопроса", max_length=1500)

    block = models.ForeignKey(QuestionsBlock, on_delete=models.CASCADE, related_name="questions")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
