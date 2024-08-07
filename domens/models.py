from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from account.models import UserFont
from notifications.create_user_notification import create_user_notification
from notifications.send_message import send_message_to_user


class Domain(models.Model):
    domain = models.CharField(max_length=50, verbose_name="домен")
    is_partners = models.BooleanField(default=True, verbose_name="партнёрский сайт")

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = "домен"
        verbose_name_plural = "домены"


class Site(models.Model):
    domain = models.ForeignKey(Domain, verbose_name="домен", on_delete=models.CASCADE, null=True)
    subdomain = models.CharField(max_length=50, verbose_name="поддомен", unique=True)
    logo = models.ImageField(verbose_name="Лого", upload_to="images/logo", null=True, blank=True)
    logo_width = models.CharField(verbose_name="ширина лого", max_length=20, null=True, blank=True)
    logo_width_mobile = models.CharField(verbose_name="ширина лого(мобильный)", max_length=20, null=True, blank=True)
    logo2 = models.ImageField(verbose_name="Лого для форм", upload_to="images/logo", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="активный", default=True)
    use_default_settings = models.BooleanField(verbose_name="Использовать общие настройки сайта", default=False)
    advertising_channel = models.CharField(verbose_name="Рекламный канал", null=True, max_length=100)
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, verbose_name="пользователь", null=True, blank=True, related_name="site"
    )

    online_from = models.DateField(verbose_name="онлайн с", default=timezone.now())

    name = models.CharField(verbose_name="Название сайта", max_length=50, null=True)
    font = models.ForeignKey(UserFont, on_delete=models.SET_NULL, null=True, verbose_name="шрифт")
    font_size = models.PositiveIntegerField(verbose_name="размер шрифта", null=True)

    owner = models.CharField(max_length=150, verbose_name="Владелец", null=True)
    contact_info = models.CharField(max_length=200, verbose_name="Контактная информация", null=True)

    class Meta:
        verbose_name = "сайт"
        verbose_name_plural = "сайты партнёров"

    def __str__(self):
        return self.subdomain

    def activate(self):
        self.is_active = True
        self.online_from = timezone.now()
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    @property
    def logo_size(self):
        width = int(self.logo_width)

        return f"{width}x{self.logo_height}px"

    @property
    def logo_height(self):
        coeff = self.logo.height / self.logo.width

        width = int(self.logo_width)

        return int(width * coeff)

    @property
    def width_percent(self):
        return int((int(self.logo_width) / 260) * 100)


def site_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        user_alert = create_user_notification(instance.user, "SITECREATED")

        send_message_to_user(instance.user.id, user_alert)


post_save.connect(site_created_handler, sender=Site)
