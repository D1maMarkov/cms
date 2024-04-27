from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.generic import View

from styles.models.common import Font

from .models.common import Page, Template
from .serializers import PageSerializer, TemplateSerializer


class ShowPage(View):
    def get(self, request, page_url):
        try:
            page = Page.objects.prefetch_related("blocks").get(url=page_url)
            serialized_page = PageSerializer(page).data

            fonts = Font.objects.all()

            return render(request, "blocks/page.html", {"page": serialized_page, "fonts": fonts})
        except Page.DoesNotExist:
            raise Http404("Page does not exist")


class ShowTemplates(View):
    def get(self, request):
        return JsonResponse(TemplateSerializer(Template.objects.all(), many=True).data)
