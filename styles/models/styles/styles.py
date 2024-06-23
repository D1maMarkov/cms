from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from blocks.models.blocks import (
    ContentBlock,
    Cover,
    FeaturesBlock,
    Navbar,
    QuestionsBlock,
    RegisterBlock,
    SocialMediaBlock,
    StagesBlock,
)
from blocks.models.catalog_block import CatalogBlock, MainPageCatalogBlock
from common.models import OneInstanceModel
from styles.models.mixins.text_mixins import (
    ExplanationTextStylesMixin,
    SubheaderStylesMixin,
)
from styles.models.styles.base_custom_styles import BaseCustomStyles


class GlobalStyles(OneInstanceModel):
    class Meta:
        verbose_name = "Глобальные стили"
        verbose_name_plural = "Глобальные стили"


class NavbarCustomStyles(BaseCustomStyles):
    block = models.OneToOneField(Navbar, on_delete=models.CASCADE, related_name="styles")


class ContentCustomStyles(BaseCustomStyles):
    block = models.OneToOneField(ContentBlock, on_delete=models.CASCADE, related_name="styles")
    border_radius = models.CharField(verbose_name="Радиус скругления картинки", null=True, blank=True, max_length=50)


class CoverCustomStyles(BaseCustomStyles):
    block = models.OneToOneField(Cover, on_delete=models.CASCADE, related_name="styles")


class FeaturesCustomStyles(BaseCustomStyles, ExplanationTextStylesMixin, SubheaderStylesMixin):
    block = models.OneToOneField(FeaturesBlock, on_delete=models.CASCADE, related_name="styles")

    columns = models.PositiveIntegerField(verbose_name="Количество колонок", default=4)
    icon_color = ColorField(verbose_name="Цвет иконок", default="#689F38")
    icon_background_color = ColorField(verbose_name="Цвет фона иконок", default="#FFFFFF")

    icon_width = models.CharField(verbose_name="Ширина иконок", max_length=20, null=True, blank=True)
    icon_height = models.CharField(verbose_name="Высота иконок", max_length=20, null=True, blank=True)


class RegisterCustomStyles(BaseCustomStyles, ExplanationTextStylesMixin):
    block = models.OneToOneField(RegisterBlock, on_delete=models.CASCADE, related_name="styles")

    button_color = ColorField(verbose_name="цвет кнопки", null=True, blank=True)


class SocialCustomStyles(BaseCustomStyles, ExplanationTextStylesMixin):
    block = models.OneToOneField(SocialMediaBlock, on_delete=models.CASCADE, related_name="styles")


class QuestionsCustomStyles(BaseCustomStyles, ExplanationTextStylesMixin):
    block = models.OneToOneField(QuestionsBlock, on_delete=models.CASCADE, related_name="styles")


class StagesCustomStyles(BaseCustomStyles, ExplanationTextStylesMixin):
    block = models.OneToOneField(StagesBlock, on_delete=models.CASCADE, related_name="styles")


class CatalogCustomStyles(BaseCustomStyles, SubheaderStylesMixin):
    block = models.OneToOneField(CatalogBlock, on_delete=models.CASCADE, related_name="styles")

    columns = models.PositiveIntegerField(verbose_name="Количество колонок", default=4)


class MainPageCatalogCustomStyles(BaseCustomStyles, SubheaderStylesMixin):
    block = models.OneToOneField(MainPageCatalogBlock, on_delete=models.CASCADE, related_name="styles")

    columns = models.PositiveIntegerField(verbose_name="Количество колонок", default=4)
    darkness_bottom = models.PositiveIntegerField(
        verbose_name="процент затемнения карточки снизу",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True,
        blank=True,
    )
    add_annotation = models.BooleanField(verbose_name="добавлять аннотацию к карточке", default=True)
    add_button = models.BooleanField(verbose_name="добавлять кнопку к карточке", default=True)
