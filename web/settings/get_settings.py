from infrastructure.persistence.models.settings import SiteSettings
from infrastructure.persistence.models.user.site import Site
from web.settings.serializers import SettingsSerializer


def get_settings(domain: str = None, subdomain: str = None) -> dict:
    if domain:
        if domain == "localhost":
            sites = Site.objects.all()
        else:
            sites = Site.objects.filter(domain__domain=domain)

        if sites.filter(subdomain=subdomain).exists():
            site = sites.get(subdomain=subdomain)
            settings = (
                SiteSettings.objects.prefetch_related("icon")
                .prefetch_related("logo")
                .prefetch_related("form_logo")
                .first()
            )
            settings = SettingsSerializer(settings).data

            if site.use_default_settings:
                return settings

            settings.pop("logo")
            settings.pop("form_logo")

            settings["site_name"] = site.name
            settings["site_font"] = site.font
            settings["site_font_size"] = site.font_size

            if site.logo:
                settings["logo"] = {
                    "image": site.logo.url,
                    "width": site.logo_width,
                    "width_mobile": site.logo_width_mobile,
                }

            if site.logo2:
                settings["form_logo"] = {
                    "image": site.logo2.url,
                    "width": site.logo_width,
                    "width_mobile": site.logo_width_mobile,
                }

            return settings

    settings = (
        SiteSettings.objects.prefetch_related("icon").prefetch_related("logo").prefetch_related("form_logo").first()
    )

    return SettingsSerializer(settings).data
