from django.http import HttpResponse
from django.views.generic import View

from domens.domain_service.domain_service import DomainService
from settings.get_settings import get_settings
from user.forms import LoginForm, ResetPasswordForm
from settings.views import SettingsMixin


class StopSite(View):
    def get(self, request):
        if self.request.user_from_header:
            self.request.user_from_header.site.deactivate()

            return HttpResponse(status=200)

        return HttpResponse(status=401)


class ActivateSite(View):
    def get(self, request):
        if self.request.user_from_header:
            self.request.user_from_header.site.activate()

            return HttpResponse(status=200)

        return HttpResponse(status=401)


class PartnerIndexPage(SettingsMixin):
    template_name = "domens/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_form"] = LoginForm()
        context["reset_password_form"] = ResetPasswordForm()

        return context
