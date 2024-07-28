from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from common.views import SubdomainMixin
from domens.models import Domain, Site
from settings.get_settings import get_settings
from user.email_service.email_service import get_email_service
from user.forms import LoginForm, RegistrationForm, ResetPasswordForm, SetPasswordForm
from user.models import User
from user.serializers import UserSerializer
from user.views.base_user_view import BaseUserView
from utils.errors import Errors, UserErrors
from utils.success_messages import Messages
from utils.validators import is_valid_email, is_valid_phone


@method_decorator(csrf_exempt, name="dispatch")
class RegisterUser(BaseUserView, SubdomainMixin):
    template_name = "user/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegistrationForm()

        return context

    @property
    def subdomain(self):
        subdomain = self.get_subdomain(self.request)
        if Site.objects.filter(subdomain=subdomain).exists():
            return Site.objects.get(subdomain=subdomain)

    @property
    def domain(self):
        domain = self.get_domain(self.request)
        if Domain.objects.filter(domain=domain).exists():
            return Domain.objects.get(domain=domain)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")

            user_with_phone = User.objects.get_user_by_phone(phone)
            user_with_email = User.objects.get_user_by_email(email)

            if user_with_email is not None and user_with_email.email_is_confirmed:
                form.add_error("email", UserErrors.username_with_email_alredy_exists.value)

                return JsonResponse({"errors": form.errors}, status=400)

            elif user_with_phone is not None and user_with_phone.phone_is_confirmed:
                form.add_error("phone", UserErrors.username_with_phone_alredy_exists.value)

                return JsonResponse({"errors": form.errors}, status=400)

            user = User.objects.create_user(
                **form.cleaned_data, register_on_site=self.subdomain, register_on_domain=self.domain
            )

            print(user)
            request.user = user
            user = authenticate(request)
            login(request, user)

            token_to_set_password = self.jwt_processor.create_set_password_token(user.id)

            return JsonResponse({"token_to_set_password": token_to_set_password})

        return JsonResponse({"errors": form.errors}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class SetPassword(BaseUserView):
    def get(self, request, token):
        form = SetPasswordForm()

        settings = get_settings(request.domain, request.subdomain)

        if request.domain == "localhost":
            domain = "localhost:8000"
        else:
            domain = Domain.objects.filter(is_partners=False).values("domain").first()["domain"]

        partner_domain = Domain.objects.filter(is_partners=True).values("domain").first()["domain"]

        return render(
            request,
            "user/set-password.html",
            {"form": form, "token": token, "settings": settings, "domain": domain, "partner_domain": partner_domain},
        )

    def post(self, request, token):
        form = SetPasswordForm(request.POST)

        if form.is_valid():
            payload = self.jwt_processor.validate_token(token)

            if not payload:
                return JsonResponse({"message": Errors.expired_set_password_token.value}, status=404)

            password = form.cleaned_data.get("password")

            user = User.objects.get_user_by_id(payload["id"])
            user.set_password(password)
            user.save()

            request.user = user
            user = authenticate(request)
            login(request, user)

            access_token = self.jwt_processor.create_access_token(user.username, user.id)

            settings = get_settings(request.domain, request.subdomain)

            if request.domain == "localhost":
                domain = "localhost:8000"
            else:
                domain = Domain.objects.filter(is_partners=False).values("domain").first()["domain"]

            partner_domain = Domain.objects.filter(is_partners=True).values("domain").first()["domain"]

            return render(
                request,
                "user/set-password.html",
                {
                    "access_token": access_token,
                    "settings": settings,
                    "domain": domain,
                    "partner_domain": partner_domain,
                },
            )

        return render(request, "user/set-password.html", {"form": form, "token": token})


class SendConfirmEmail(BaseUserView):
    def __init__(self):
        super().__init__()
        self.email_service = get_email_service(self.jwt_processor)

    def get(self, request):
        user = request.user_from_header

        if user:
            self.email_service.send_mail_to_confirm_email(user)

        return HttpResponse(status=200)


@method_decorator(csrf_exempt, name="dispatch")
class Login(BaseUserView):
    template_name = "user/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()

        return context

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_or_email = form.cleaned_data.get("phone_or_email")
            password = form.cleaned_data.get("password")

            if is_valid_phone(phone_or_email):
                user = User.objects.get_user_by_phone(phone_or_email)
                if user is None:
                    form.add_error("phone_or_email", UserErrors.user_by_phone_not_found.value)

                    return JsonResponse({"errors": form.errors}, status=400)

            elif is_valid_email(phone_or_email):
                user = User.objects.get_user_by_email(phone_or_email)
                if user is None:
                    form.add_error("phone_or_email", UserErrors.user_by_email_not_found.value)

                    return JsonResponse({"errors": form.errors}, status=400)

            else:
                form.add_error("phone_or_email", UserErrors.incorrect_login.value)

                return JsonResponse({"errors": form.errors}, status=400)

            if not user.verify_password(password):
                form.add_error("password", UserErrors.incorrect_password.value)

                return JsonResponse({"errors": form.errors}, status=400)

            access_token = self.jwt_processor.create_access_token(user.username, user.id)
            request.user = user
            user = authenticate(request)
            login(request, user)

            return JsonResponse({"acess_token": access_token})

        return JsonResponse({"errors": form.errors}, status=400)


class GetUserInfo(View):
    def get(self, request):
        user_from_request = request.user
        user_from_header = request.user_from_header

        user = None
        if user_from_header:
            user = user_from_header
        if user_from_request.is_authenticated:
            user = user_from_request

        if user:
            user = UserSerializer(user).data
            return JsonResponse(user)
        else:
            return HttpResponse(status=401)


class ConfirmEmail(BaseUserView):
    def get(self, request, token):
        payload = self.jwt_processor.validate_token(token)

        if not payload:
            return render(
                request,
                "user/confirm_email.html",
                {"message", "Ссылка больше неактивна :/ \n попробуйте получить письмо ещё раз"},
            )

        user = User.objects.get_user_by_id(payload["user_id"])
        user.confirm_email()

        return render(request, "user/confirm_email.html", {"message": "Почта подтверждена!"})


@method_decorator(csrf_exempt, name="dispatch")
class SendMailToResetPassword(BaseUserView):
    template_name = "user/reset-password.html"

    def __init__(self):
        super().__init__()
        self.email_service = get_email_service(self.jwt_processor)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ResetPasswordForm()

        return context

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")

            user = User.objects.get_user_by_email(email)
            if user is None:
                form.add_error("email", UserErrors.user_by_email_not_found.value)
                return JsonResponse({"errors": form.errors})

            self.email_service.send_mail_to_reset_password(user)

            return JsonResponse({"message": Messages.sent_message_to_reset_password.value})

        return JsonResponse({"errors": form.errors}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class SetToken(BaseUserView):
    template_name = "user/set-token.html"

    def get(self, request, token):
        payload = self.jwt_processor.validate_token(token)
        if payload:
            user = User.objects.get_user_by_id(payload["id"])
            request.user = user
            user = authenticate(request)
            login(request, user)

            return render(request, "user/set-token.html", {"token": token})

        return HttpResponse(status=401)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")
