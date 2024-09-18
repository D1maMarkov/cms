from django.apps import AppConfig


class SystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "web.system"

    verbose_name = "Система"
