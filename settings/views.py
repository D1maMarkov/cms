from django.views.generic import TemplateView

from domens.domain_service.domain_service import DomainService
from settings.get_settings import get_settings


class SettingsMixin(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.domain == "localhost":
            domain = "localhost:8000"
        else:
            domain = DomainService.get_domain_string()

        context["domain"] = domain
        context["settings"] = get_settings(self.request)
        context["partner_domain"] = DomainService.get_partners_domain_string()

        return context
