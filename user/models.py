from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save, pre_save

from domens.domain_service.domain_service import DomainService
from domens.models import Site
from emails.email_service.email_service import get_email_service
from notifications.create_user_notification import create_user_notification
from notifications.send_message import send_message_to_user
from user.user_manager.user_manager import UserManager
from user.user_manager.user_manager_interface import UserManagerInterface


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name="Имя пользователя", max_length=100)
    second_name = models.CharField(verbose_name="Фамлия", max_length=200, null=True, blank=True)

    phone = models.CharField(verbose_name="Номер телефона", max_length=12, null=True)
    phone_is_confirmed = models.BooleanField(verbose_name="Телефон подтвержден", default=False)

    email = models.CharField(verbose_name="E-mail", max_length=200, null=True)
    new_email = models.CharField(verbose_name="новый E-main", max_length=200, null=True, blank=True)
    email_is_confirmed = models.BooleanField(verbose_name="Почта подтверждена", default=False)

    created_at = models.DateTimeField(verbose_name="пользователь создан", auto_now_add=True, null=True)

    profile_picture = models.ImageField(verbose_name="аватарка", null=True, blank=True)

    register_on_site = models.ForeignKey(
        "domens.Site",
        verbose_name="зарегистрирован на сайте",
        related_name="register_on_site",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    register_on_domain = models.ForeignKey(
        "domens.Domain",
        verbose_name="зарегистрирован на домене",
        related_name="register_on_domain",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "id"

    staff = models.BooleanField(default=False)

    objects: UserManagerInterface = UserManager()

    @property
    def is_staff(self):
        return self.staff

    @property
    def full_site_name(self) -> str | None:
        if Site.objects.filter(user_id=self.id).exists():
            return f"{self.site}.{DomainService.get_partners_domain_string()}"

        return None

    def __str__(self) -> str:
        return self.username

    def verify_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)

    def confirm_email(self) -> None:
        self.email_is_confirmed = True
        self.save()

    def change_email(self, new_email: str) -> None:
        if self.email_is_confirmed:
            self.new_email = new_email

        else:
            self.email = new_email

        self.save()

    def confirm_new_email(self) -> None:
        self.email = self.new_email
        self.new_email = None
        self.email_is_confirmed = True
        self.save()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


def user_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        email_service = get_email_service()
        email_service.send_mail_to_confirm_email(instance)

        user_alert = create_user_notification(instance, "SIGNEDUP")
        send_message_to_user(instance.id, user_alert)


def user_verified_email_handler(sender, instance, *args, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = User.objects.get_user_by_id(id=instance.id)
        if not previous.email_is_confirmed and instance.email_is_confirmed:
            user_alert = create_user_notification(instance, "EMAILVERIFIED")
            send_message_to_user(instance.id, user_alert)


def user_change_email_handler(sender, instance, *args, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = User.objects.get_user_by_id(id=instance.id)

        email_service = get_email_service()

        if not previous.new_email and instance.new_email:
            email_service.send_mail_to_confirm_new_email(instance)
            return

        if previous.email != instance.email:
            email_service.send_mail_to_confirm_email(instance)
            return


post_save.connect(user_created_handler, sender=User)
pre_save.connect(user_verified_email_handler, sender=User)
pre_save.connect(user_change_email_handler, sender=User)
