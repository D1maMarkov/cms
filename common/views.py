import re

from django.db.models import Q
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView

from domens.models import Domain, Site
from settings.get_settings import get_settings
from settings.models import SiteSettings


class BaseTemplateView(TemplateView):
    def get_domain(self):
        host = self.request.get_host()
        host = host.replace("127.0.0.1", "localhost")
        if ":" in host:
            host = host.split(":")[0]

        subdomain = self.get_subdomain()
        first_domain = host.split(".")[-1]
        print(first_domain)

        domain = re.findall(f"{subdomain}.*?{first_domain}", host)[0]
        domain = re.sub(subdomain, "", domain)
        if domain[0] == ".":
            domain = domain[1::]

        return domain

    def get_subdomain(self):
        host = self.request.get_host()
        host = host.replace("127.0.0.1", "localhost")

        if "localhost" in host:
            if "." not in host:
                return ""

            return host.split(".")[0]

        if host.count(".") < 2:
            return ""

        return host.split(".")[0]

    def valid_subdomen(self, subdomain: str) -> bool:
        if not subdomain:
            return True

        if Site.objects.filter(subdomain=subdomain).exists() and Site.objects.get(subdomain=subdomain).is_active:
            return True

        if subdomain == "www":
            return True

        return False

    def get(self, *args, **kwargs):
        subdomain = self.get_subdomain()
        domain = self.get_domain()

        print(domain, "domain")
        print(subdomain, "subdomain")

        self.settings = get_settings(domain, subdomain)

        if not self.valid_subdomen(subdomain):
            return HttpResponseNotFound("404 Subdomen not found")

        if (
            domain != "localhost"
            and subdomain
            and not Site.objects.filter(Q(domain__domain=domain) & Q(subdomain=subdomain)).exists()
        ):
            return HttpResponseNotFound("404 Subdomen not found")

        partner_domain = Domain.objects.filter(is_partners=True).first()
        if domain == partner_domain.domain and not subdomain and self.request.path != "":
            return HttpResponseNotFound("404 Page not found")
        
        if domain == partner_domain.domain and SiteSettings.objects.first().disable_partners_sites:
            return HttpResponseNotFound("404 Page not found")

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["settings"] = self.settings
        if self.get_domain() == "localhost":
            context["domain"] = "localhost:8000"
        else:
            context["domain"] = Domain.objects.filter(is_partners=False).first().domain

        return context
