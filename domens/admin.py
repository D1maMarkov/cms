from django.contrib import admin
from django.contrib.admin.decorators import register

from domens.models import Domain, Site


@register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass


@register(Domain)
class DomainAdmin(admin.ModelAdmin):
    pass
