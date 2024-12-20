import json

from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from infrastructure.persistence.models.settings import Font, UserFont
from infrastructure.persistence.models.styles.colors.colors import ColorStyles
from infrastructure.persistence.models.styles.other import IconSize, MarginBlock
from infrastructure.persistence.models.styles.texts.texts import (
    ExplanationText,
    HeaderText,
    MainText,
    SubheaderText,
)

from .serializers import (
    ColorsSerializer,
    FontSerializer,
    IconSizeSerializer,
    MarginBlockSerializer,
    TextSerializer,
)


class GetColorStyles(View):
    def get(self, request):
        color_styles = ColorStyles.objects.first()
        return JsonResponse(ColorsSerializer(color_styles).data)


class GetHeaderStyles(View):
    def get(self, request):
        header_styles = HeaderText.objects.first()
        return JsonResponse(TextSerializer(header_styles).data)


class GetMainTextStyles(View):
    def get(self, request):
        main_text_styles = MainText.objects.first()
        return JsonResponse(TextSerializer(main_text_styles).data)


class GetSubheaerStyles(View):
    def get(self, request):
        header_styles = SubheaderText.objects.first()
        return JsonResponse(TextSerializer(header_styles).data)


class GetExplanationTextStyles(View):
    def get(self, request):
        explanation_text_styles = ExplanationText.objects.first()
        return JsonResponse(TextSerializer(explanation_text_styles).data)


class GetMarginBlock(View):
    def get(self, request):
        margins = MarginBlock.objects.first()
        return JsonResponse(MarginBlockSerializer(margins).data)


class GetIconSize(View):
    def get(self, request):
        icon_size = IconSize.objects.first()
        return JsonResponse(IconSizeSerializer(icon_size).data)


class GetFonts(View):
    def get(self, request):
        fonts = [*Font.objects.exclude(link=None), *UserFont.objects.exclude(link=None)]
        return HttpResponse(json.dumps(FontSerializer(fonts, many=True).data))
