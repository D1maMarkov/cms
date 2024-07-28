from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import MultipleObjectsReturned

from user.user_manager.user_manager_interface import UserManagerInterface


class UserManager(BaseUserManager, UserManagerInterface):
    def get_by_natural_key(self, username):
        user_by_email = self.get_user_by_email(username)
        user_by_phone = self.get_user_by_phone(username)

        if user_by_email:
            return user_by_email

        if user_by_phone:
            return user_by_phone

    def get_user_by_id(self, id: int):
        try:
            return self.get(id=id)
        except self.model.DoesNotExist:
            return None

    def get_user_by_email(self, email: str):
        try:
            return self.get(**{"email": email})
        except self.model.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            last_user = self.get_queryset().first()
            users_with_email_exclude_last = self.get_queryset().exclude(created_at=last_user.created_at)
            users_with_email_exclude_last.update(email=None)

            return last_user

    def get_user_by_phone(self, phone: str):
        try:
            return self.get(**{"phone": phone})
        except self.model.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            last_user = self.get_queryset().first()
            users_with_phone_exclude_last = self.get_queryset().exclude(created_at=last_user.created_at)
            users_with_phone_exclude_last.update(phone=None)

            return last_user

    def create_user(self, username: str, phone: str, email: str, **extra_fields):
        return self.model.objects.create(username=username, email=email, phone=phone, **extra_fields)

    def create_superuser(self, username: str, phone: str, email: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, phone, email, **extra_fields)
