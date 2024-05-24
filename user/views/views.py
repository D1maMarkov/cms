import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from common.views import BaseTemplateView
from user.email_service.email_service import get_email_service
from user.forms import LoginForm, RegistrationForm, ResetPasswordForm, SetPasswordForm
from user.serializers import UserSerializer
from user.views.base_user_view import BaseUserView
from utils.errors import Errors, UserErrors
from utils.success_messages import Messages
from utils.validators import is_valid_phone


@method_decorator(csrf_exempt, name="dispatch")
class RegisterUser(BaseUserView):
    template_name = "user/register.html"

    def __init__(self):
        super().__init__()
        self.email_service = get_email_service(self.jwt_processor)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegistrationForm()

        return context

    def post(self, request):
        form = RegistrationForm(json.loads(request.body))
        if form.is_valid():
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")

            user_with_phone = self.user_manager.get_user_by_phone(phone)
            user_with_email = self.user_manager.get_user_by_email(email)

            if user_with_email is not None and user_with_email.email_is_confirmed:
                form.add_error("email", UserErrors.username_with_email_alredy_exists.value)

                return JsonResponse({"errors": form.errors}, status=400)

            elif user_with_phone is not None:
                form.add_error("phone", UserErrors.username_with_phone_alredy_exists.value)

                return JsonResponse({"errors": form.errors}, status=400)

            user = self.user_manager.create_user(form.cleaned_data)
            self.email_service.send_mail_to_confirm_email(user)

            token_to_set_password = self.jwt_processor.create_set_password_token(user.id)

            return JsonResponse({"token_to_set_password": token_to_set_password})

        return JsonResponse({"errors": form.errors}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class SetPassword(BaseUserView):
    def get(self, request, token):
        form = SetPasswordForm()
        return render(request, "user/set-password.html", {"form": form, "token": token})

    def post(self, request, token):
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            payload = self.jwt_processor.validate_token(token)

            if not payload:
                return JsonResponse({"message": Errors.expired_set_password_token.value}, status=404)

            password = form.cleaned_data.get("password")

            user = self.user_manager.get_user_by_id(payload["id"])
            user.set_password(password)
            user.save()

            access_token = self.jwt_processor.create_access_token(user.username, user.id)

            return render(request, "user/set-password.html", {"access_token": access_token})

        return render(request, "user/set-password.html", {"form": form, "token": token})


@method_decorator(csrf_exempt, name="dispatch")
class Login(BaseUserView):
    template_name = "user/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()

        return context

    def post(self, request):
        form = LoginForm(json.loads(request.body))
        if form.is_valid():
            phone_or_email = form.cleaned_data.get("phone_or_email")
            password = form.cleaned_data.get("password")

            if is_valid_phone(phone_or_email):
                user = self.user_manager.get_user_by_phone(phone_or_email)
                if user is None:
                    form.add_error("phone_or_email", UserErrors.user_by_phone_not_found.value)

                    return JsonResponse({"errors": form.errors}, status=400)

            else:
                user = self.user_manager.get_user_by_email(phone_or_email)
                if user is None:
                    form.add_error("phone_or_email", UserErrors.user_by_email_not_found.value)

                    return JsonResponse({"errors": form.errors}, status=400)

            if not user.verify_password(password):
                form.add_error("password", UserErrors.incorrect_password.value)

                return JsonResponse({"errors": form.errors}, status=400)

            access_token = self.jwt_processor.create_access_token(user.username, user.id)

            return JsonResponse({"acess_token": access_token})

        return JsonResponse({"errors": form.errors}, status=400)


class Profile(BaseTemplateView):
    template_name = "user/profile.html"


class GetUserInfo(BaseUserView):
    def get(self, request):
        token = request.headers.get("Authorization")
        payload = self.jwt_processor.validate_token(token)
        user = None

        if payload:
            user = self.user_manager.get_user_by_id(payload["id"])
            user = UserSerializer(user).data

        return JsonResponse(user)


class ConfirmEmail(BaseUserView):
    def get(self, request, token):
        payload = self.jwt_processor.validate_token(token)

        if not payload:
            return render(
                request,
                "user/confirm_email.html",
                {"message", "Ссылка больше неактивна :/ \n попробуйте получить письмо ещё раз"},
            )

        user = self.user_manager.get_user_by_id(payload["user_id"])
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
        form = ResetPasswordForm(json.loads(request.body))
        if form.is_valid():
            email = form.cleaned_data.get("email")

            user = self.user_manager.get_user_by_email(email)
            if user is None:
                form.add_error("email", UserErrors.user_by_email_not_found.value)
                return JsonResponse({"errors": form.errors})

            self.email_service.send_mail_to_reset_password(user)

            return JsonResponse({"message": Messages.sent_message_to_reset_password.value})

        return JsonResponse({"errors": form.errors}, status=400)