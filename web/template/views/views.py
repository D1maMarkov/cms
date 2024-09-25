from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views import View

from application.common.url_parser import UrlParserInterface
from application.services.domains.url_parser import get_url_parser
from domain.products.repository import ProductRepositoryInterface
from domain.user.exceptions import InvalidReferalLevel, InvalidSortedByField
from domain.user_sessions.repository import UserSessionRepositoryInterface
from infrastructure.persistence.models.blocks.catalog_block import CatalogBlock
from infrastructure.persistence.models.blocks.common import Page
from infrastructure.persistence.repositories.product_repository import (
    get_product_repository,
)
from infrastructure.persistence.repositories.user_session_repository import (
    get_user_session_repository,
)
from web.account.views.templates import Profile
from web.blocks.views import ShowPage
from web.catalog.views import ShowCatalogPage
from web.domens.views.mixins import SubdomainMixin
from web.template.profile_template_loader.profile_template_loader import (
    get_profile_template_loader,
)
from web.template.profile_template_loader.profile_template_loader_interface import (
    ProfileTemplateLoaderInterface,
)
from web.template.template_loader.tempate_context_processor.template_context_processor import (
    get_template_context_processor,
)
from web.template.template_loader.template_loader import get_template_loader
from web.template.template_loader.template_loader_interface import (
    TemplateLoaderInterface,
)


def slug_router(request, slug):
    if Page.objects.filter(url=slug).exists():
        return ShowPage.as_view()(request, page_url=slug)

    if CatalogBlock.objects.filter(product_type__slug=slug).exists():
        return ShowCatalogPage.as_view()(request, products_slug=slug)

    if slug == "my":
        return Profile.as_view()(request)

    return PageNotFound.as_view()(request)


class BaseTemplateLoadView(View):
    template_loader: TemplateLoaderInterface = get_template_loader(get_template_context_processor())

    def get(self, request):
        template = self.get_content(request)
        return JsonResponse({"content": template})


class GetChangeUserFormTemplate(BaseTemplateLoadView):
    url_parser: UrlParserInterface = get_url_parser()
    user_session_repository = get_user_session_repository()

    def get_content(self, request: HttpRequest):
        adress = self.url_parser.remove_protocol(request.META.get("HTTP_REFERER"))

        self.user_session_repository.create_user_action(
            adress=adress,
            text=f"""Открыл данные профиля""",
            session_unique_key=request.session["user_activity"]["unique_key"],
        )
        return self.template_loader.load_change_user_form(request)


class GetChangeSiteFormTemplate(BaseTemplateLoadView):
    url_parser: UrlParserInterface = get_url_parser()
    user_session_repository = get_user_session_repository()

    def get_content(self, request: HttpRequest):
        adress = self.url_parser.remove_protocol(request.META.get("HTTP_REFERER"))

        self.user_session_repository.create_user_action(
            adress=adress,
            text="Открыл настройку партнерского сайта",
            session_unique_key=request.session["user_activity"]["unique_key"],
        )

        return self.template_loader.load_change_site_form(request)


class GetChangeSocialsFormTemplate(BaseTemplateLoadView):
    def get_content(self, request):
        return self.template_loader.load_change_socials_form(request)


class PageNotFound(SubdomainMixin):
    template_name = "common/404.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(), status=404)


class ProfileTemplate(View):
    template_loader: ProfileTemplateLoaderInterface = get_profile_template_loader()

    def get(self, request):
        return JsonResponse(self.template_loader.load_profile_template(request))


class RefsTemplate(View):
    template_loader: ProfileTemplateLoaderInterface = get_profile_template_loader()

    def get(self, request):
        try:
            return JsonResponse(self.template_loader.load_refs_template(request))
        except (InvalidSortedByField, InvalidReferalLevel) as e:
            return JsonResponse({"error": str(e)}, status=400)


class IdeasTemplate(View):
    template_loader: ProfileTemplateLoaderInterface = get_profile_template_loader()

    def get(self, request):
        try:
            return JsonResponse(self.template_loader.load_ideas_template(request))
        except (InvalidSortedByField, InvalidReferalLevel) as e:
            return JsonResponse({"error": str(e)}, status=400)


class ManualsTemplate(View):
    template_loader: ProfileTemplateLoaderInterface = get_profile_template_loader()

    def get(self, request):
        return JsonResponse(self.template_loader.load_manuals_template(request))


class SiteTemplate(View):
    template_loader: ProfileTemplateLoaderInterface = get_profile_template_loader()

    def get(self, request):
        return JsonResponse(self.template_loader.load_site_template(request))


class UserProductsTemplate(View):
    template_loader: ProfileTemplateLoaderInterface = get_profile_template_loader()

    def get(self, request):
        return JsonResponse(self.template_loader.load_products_template(request))


class GetChoiceProductForm(BaseTemplateLoadView):
    url_parser: UrlParserInterface = get_url_parser()
    user_session_repository = get_user_session_repository()

    def get_content(self, request):
        adress = self.url_parser.remove_protocol(request.META.get("HTTP_REFERER"))
        self.user_session_repository.create_user_action(
            adress=adress,
            text="Открыл список продуктов",
            session_unique_key=request.session["user_activity"]["unique_key"],
        )

        return self.template_loader.load_choice_product_form(request)


class GetCreateUserProductForm(BaseTemplateLoadView):
    def get_content(self, request: HttpRequest):
        return self.template_loader.load_create_user_product_form(request)


class GetProductDescriptionPopup(BaseTemplateLoadView):
    url_parser: UrlParserInterface = get_url_parser()
    user_session_repository: UserSessionRepositoryInterface = get_user_session_repository()
    product_repository: ProductRepositoryInterface = get_product_repository()

    def get_content(self, request: HttpRequest):
        adress = self.url_parser.remove_protocol(request.META.get("HTTP_REFERER"))

        product = int(request.GET.get("product"))

        product_name = self.product_repository.get_product_by_id(product)

        self.user_session_repository.create_user_action(
            adress=adress,
            text=f'''Открыл описание продукта "{product_name}"''',
            session_unique_key=request.session["user_activity"]["unique_key"],
        )

        return self.template_loader.load_product_description_popup(request)


class GetDeleteProductPopup(BaseTemplateLoadView):
    def get_content(self, request):
        return self.template_loader.load_delete_product_popup(request)


class GetReferralPopupTemplate(BaseTemplateLoadView):
    def get_content(self, request):
        return self.template_loader.load_referral_popup(request)


class GetCreateIdeaForm(BaseTemplateLoadView):
    def get_content(self, request):
        return self.template_loader.load_create_idea_form(request)
