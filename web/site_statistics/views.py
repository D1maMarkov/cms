from django.http import HttpRequest, HttpResponse
from django.views.generic import View

from application.sessions.add_session_action import (
    IncrementSessionCount,
    get_increment_session_count,
)
from application.sessions.raw_session_service import get_raw_session_service
from application.texts.user_session import UserActions
from domain.products.repository import ProductRepositoryInterface
from infrastructure.logging.user_activity.create_session_log import (
    CreateUserSesssionLog,
    get_create_user_session_log,
)
from infrastructure.persistence.repositories.product_repository import (
    get_product_repository,
)
from infrastructure.requests.request_interface import RequestInterface
from infrastructure.requests.service import get_request_service
from web.settings.views.settings_mixin import SettingsMixin
from web.styles.views import StylesMixin


class OpenedProductPopupView(View):
    product_repository: ProductRepositoryInterface = get_product_repository()
    increment_session_profile_action: IncrementSessionCount = get_increment_session_count("profile_actions_count")
    create_user_session_log: CreateUserSesssionLog = get_create_user_session_log()

    def get(self, request: HttpRequest) -> HttpResponse:
        product = int(request.GET.get("product_id")) - 1
        adress = request.META.get("HTTP_REFERER").split("/")[-1]

        product_name = self.product_repository.get_product_name_from_catalog(
            product_type_slug=adress.split("/")[1], product_index=product
        )

        self.increment_session_profile_action(request=request)
        self.create_user_session_log(request=request, text=f'''Открыл описание "{product_name}"''')

        return HttpResponse(status=201)


class OpenedProductLinkView(View):
    product_repository: ProductRepositoryInterface = get_product_repository()
    increment_banks_count: IncrementSessionCount = get_increment_session_count("banks_count")
    create_user_session_log: CreateUserSesssionLog = get_create_user_session_log()

    def get(self, request: HttpRequest) -> HttpResponse:
        product = int(request.GET.get("product_id")) - 1
        adress = request.META.get("HTTP_REFERER").split("/")[-1]

        product_name = self.product_repository.get_product_name_from_catalog(
            product_type_slug=adress.split("/")[1], product_index=product
        )

        self.increment_banks_count(request=request)
        self.create_user_session_log(request=request, text=f'''Перешел по ссылке "{product_name}"''')

        return HttpResponse(status=201)


class OpenedProductPromoView(View):
    product_repository: ProductRepositoryInterface = get_product_repository()
    increment_banks_count: IncrementSessionCount = get_increment_session_count("banks_count")
    create_user_session_log: CreateUserSesssionLog = get_create_user_session_log()

    def get(self, request: HttpRequest) -> HttpResponse:
        product = int(request.GET.get("product_id")) - 1

        product_name = self.product_repository.get_offers()[product]  # type: ignore

        self.increment_banks_count(request=request)
        self.create_user_session_log(request=request, text=f'''Перешел по баннеру "{product_name}"''')

        return HttpResponse(status=201)


class OpenedChangePasswordFormView(View):
    increment_session_profile_action: IncrementSessionCount = get_increment_session_count("profile_actions_count")
    create_user_session_log: CreateUserSesssionLog = get_create_user_session_log()

    def get(self, request: HttpRequest) -> HttpResponse:
        self.increment_session_profile_action(request=request)
        self.create_user_session_log(request=request, text=UserActions.opened_password_change)

        return HttpResponse(status=201)


class OpenedUpdateProductFormView(View):
    product_repository: ProductRepositoryInterface = get_product_repository()
    increment_session_profile_action: IncrementSessionCount = get_increment_session_count("profile_actions_count")
    create_user_session_log: CreateUserSesssionLog = get_create_user_session_log()

    def get(self, request: HttpRequest) -> HttpResponse:
        product = self.product_repository.get(id=int(request.GET.get("product")))

        product_name = product.name if product else ""

        self.increment_session_profile_action(request=request)
        self.create_user_session_log(request=request, text=f'''Открыл настройку продукта "{product_name}"''')

        return HttpResponse(status=201)


class IncrementBanksCountView(View):
    increment_banks_count: IncrementSessionCount = get_increment_session_count("banks_count")
    create_user_session_log: CreateUserSesssionLog = get_create_user_session_log()

    def get(self, request: HttpRequest) -> HttpResponse:
        self.increment_banks_count(request=request)
        self.create_user_session_log(request=request, text=UserActions.opened_product_description)

        return HttpResponse(status=200)


class CapchaView(SettingsMixin, StylesMixin):
    template_name = "common/capcha.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs) | self.get_styles_context()


class SubmitCapcha(View):
    def post(self, request: RequestInterface) -> HttpResponse:
        if request.raw_session:
            raw_session_service = get_raw_session_service(get_request_service(request))
            print(request.raw_session)
            raw_session_service.success_capcha(request.raw_session)

        return HttpResponse(status=200)
