from django.db import models

from user.models import User


class Trigger(models.Model):
    name = models.CharField(verbose_name="триггер", max_length=100)

    class Meta:
        verbose_name = "триггер"
        verbose_name_plural = "триггеры"

    def __str__(self):
        return self.name


class Notification(models.Model):
    name = models.CharField(verbose_name="название", max_length=300)
    message = models.CharField(verbose_name="сообщение", max_length=600)

    statuses = (
        ("warning", "предупреждение"),
        ("error", "ошибка"),
        ("info", "информационное"),
    )

    status = models.CharField(choices=statuses, verbose_name="статус", max_length=100, null=True)
    trigger = models.ForeignKey(Trigger, on_delete=models.SET_NULL, null=True, verbose_name="триггер")

    class Meta:
        verbose_name = "уведомление"
        verbose_name_plural = "уведомления"

    def __str__(self):
        return self.name


class UserNotification(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, verbose_name="уведомление")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания", null=True)

    class Meta:
        verbose_name = "пользовательское уведомление"
        verbose_name_plural = "пользовательские уведомления"

    def __str__(self):
        return f"{self.notification.name}"
