from django.contrib import admin
from django.contrib.admin.decorators import register

from .models.colors.colors import ColorStyles
from .models.common import (
    ContentCustomStyles,
    CoverCustomStyles,
    GlobalStyles,
    NavbarCustomStyles,
)
from .models.font import Font
from .models.other_styles import IconSize, MarginBlock
from .models.texts import ExplanationText, HeaderText, MainText, SubheaderText


class StyleInline(admin.StackedInline):
    extra = 0
    max_num = 1


class NavbarCustomStylesInline(StyleInline):
    model = NavbarCustomStyles


class ContentCustomStylesInline(StyleInline):
    model = ContentCustomStyles


class CoverCustomStylesInline(StyleInline):
    model = CoverCustomStyles


class ColorStylesInline(StyleInline):
    model = ColorStyles


class HeaderTextInline(StyleInline):
    model = HeaderText


class MainTextInline(StyleInline):
    model = MainText


class SubheaderTextInline(StyleInline):
    model = SubheaderText


class ExplanationTextInline(StyleInline):
    model = ExplanationText


class MarginBlockInline(StyleInline):
    model = MarginBlock


class IconSizeInline(StyleInline):
    model = IconSize


@register(Font)
class FontAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]


@register(GlobalStyles)
class GlobalStylesAdmin(admin.ModelAdmin):
    inlines = [
        ColorStylesInline,
        HeaderTextInline,
        MainTextInline,
        SubheaderTextInline,
        ExplanationTextInline,
        MarginBlockInline,
        IconSizeInline,
    ]