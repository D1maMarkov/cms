import json

from django.http import HttpResponse, JsonResponse

from account.forms import (
    AddUserProductForm,
    ChangeSiteForm,
    ChangeSocialsForm,
    ChangeUserForm,
)
from account.models import Messanger, UserMessanger, UserSocialNetwork
from account.usecases.user_products.add_user_product import AddUserProduct
from common.views import FormView
from domens.domain_service.domain_service import get_domain_service
from domens.domain_service.domain_service_interface import DomainServiceInterface
from infrastructure.persistence.repositories.product_repository import (
    get_product_repository,
)
from settings.models import SocialNetwork, UserFont
from user.exceptions import UserProductAlreadyExists
from user.models.site import Site
from user.models.user import User
from user.views.base_user_view import APIUserRequired
from utils.errors import UserErrors


class ChangeSiteView(FormView):
    domain_service: DomainServiceInterface = get_domain_service()
    form_class = ChangeSiteForm

    def form_valid(self, request, form):
        user = request.user_from_header
        if user is None:
            return HttpResponse(status=401)

        site_url = form.cleaned_data.get("site")
        if Site.objects.filter(user_id=user.id).exists():
            site = user.site
        else:
            site = Site.objects.create(
                subdomain=form.cleaned_data["site"],
                name=form.cleaned_data["name"],
                owner=form.cleaned_data["owner"],
                contact_info=form.cleaned_data["contact_info"],
                font=UserFont.objects.get(id=form.cleaned_data["font"]),
                font_size=form.cleaned_data["font_size"],
                user=user,
                domain=self.domain_service.get_domain_model_by_id(int(form.cleaned_data.get("domain"))),
            )

        if site.subdomain != site_url and Site.objects.filter(subdomain=site_url).exists():
            form.add_error("site", "Такой адрес уже существует")
            return JsonResponse({"errors": form.errors}, status=400)

        site.subdomain = form.cleaned_data["site"]
        site.name = form.cleaned_data["name"]
        site.owner = form.cleaned_data["owner"]
        site.contact_info = form.cleaned_data["contact_info"]

        site.font = UserFont.objects.get(id=form.cleaned_data["font"])
        site.font_size = form.cleaned_data["font_size"]

        logo = form.cleaned_data.get("logo", None)
        if logo:
            site.logo = logo

        if form.cleaned_data.get("delete_logo") == "true":
            site.logo = None

        site.logo_width = int(260 * (form.cleaned_data["logo_size"] / 100))

        site.save()

        return HttpResponse(status=200)


class ChangeSocialsView(FormView):
    form_class = ChangeSocialsForm

    def form_valid(self, request, form):
        user = request.user_from_header
        if user is None:
            return HttpResponse(status=401)

        site = user.site

        user_social_networks = json.loads(form.cleaned_data.get("socials"))
        social_networks_ids = [user_social_network["social"] for user_social_network in user_social_networks]

        if len({social_network["social"] for social_network in user_social_networks}) < len(user_social_networks):
            form.add_error("socials", "Вы можете указать только один канал для каждой соц. сети")
            return JsonResponse({"errors": form.errors}, status=400)

        all_social_networks = SocialNetwork.objects.all()

        for social_network in all_social_networks:
            if (
                UserSocialNetwork.objects.filter(site=site, social_network=social_network).exists()
                and social_network.id not in social_networks_ids
            ):
                UserSocialNetwork.objects.filter(site=site, social_network=social_network).delete()

        if user_social_networks:
            for user_social_network in user_social_networks:
                social_network = SocialNetwork(id=user_social_network["social"])

                user_social_network, created = UserSocialNetwork.objects.update_or_create(
                    social_network=social_network,
                    site=site,
                    defaults={"adress": user_social_network["adress"]},
                )

        return HttpResponse(status=200)


class ChangeUserView(FormView):
    form_class = ChangeUserForm

    def form_valid(self, request, form):
        if request.user_from_header is None:
            return HttpResponse(status=401)

        user = request.user_from_header

        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")

        user_with_phone = User.objects.get_user_by_phone(phone)
        user_with_email = User.objects.get_user_by_email(email)

        if user_with_email != user and user_with_email and user_with_email.email_is_confirmed:
            form.add_error("email", UserErrors.username_with_email_alredy_exists.value)

            return JsonResponse({"errors": form.errors}, status=400)

        elif user_with_phone != user and user_with_phone and user_with_phone.phone_is_confirmed:
            form.add_error("phone", UserErrors.username_with_phone_alredy_exists.value)

            return JsonResponse({"errors": form.errors}, status=400)

        user.username = form.cleaned_data.get("username")
        user.second_name = form.cleaned_data.get("second_name")
        user.phone = phone

        if form.cleaned_data.get("social_network"):
            social_network = form.cleaned_data.get("social_network")
            adress = form.cleaned_data.get("adress")

            messanger = Messanger.objects.get(id=social_network)

            UserMessanger.objects.update_or_create(user_id=user.id, defaults={"messanger": messanger, "adress": adress})

        if form.cleaned_data.get("profile_picture"):
            user.profile_picture = form.cleaned_data.get("profile_picture")

        if user.email_is_confirmed and email != user.email:
            user.change_email(email)
            user.save()

            return JsonResponse(
                {
                    "info": {
                        "title": "Вы меняете email",
                        "text": "На новый email адрес отправлено письмо со ссылкой для подтверждения",
                    }
                },
                status=202,
            )

        user.change_email(email)
        user.save()

        return HttpResponse(status=200)


class AddUserProductView(FormView, APIUserRequired):
    form_class = AddUserProductForm
    add_user_product_interactor = AddUserProduct(get_product_repository())

    def form_valid(self, request, form):
        print(request.POST, request.FILES)

        user = request.user
        print(request.user)

        try:
            self.add_user_product_interactor(form.cleaned_data, user)
        except UserProductAlreadyExists as e:
            return JsonResponse({"errors": str(e)})

        """product = form.cleaned_data.get("product")
        product = Product.objects.get(id=product)

        try:
            UserProduct.objects.update_or_create(
                product=product,
                user=request.user,
                defaults={
                    "link": form.cleaned_data.get("link"),
                    "comment": form.cleaned_data.get("comment"),
                    "connected": form.cleaned_data.get("connected"),
                    "profit": form.cleaned_data.get("profit"),
                    "got": form.cleaned_data.get("got"),
                    "screen": form.cleaned_data.get("screen"),
                    "connected_with_link": form.cleaned_data.get("connected_with_link") == "true",
                    "deleted": False,
                },
            )
        except UserProductAlreadyExists:
            return JsonResponse({"errors": f'Вы уже добавили себе продукт "{product}"'})"""

        return HttpResponse(status=200)