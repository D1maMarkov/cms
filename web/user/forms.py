from django import forms

from application.texts.errors import UserErrorsMessages
from domain.user.validator import UserValidatorInterface
from infrastructure.user.validator import get_user_validator


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Ваше имя"}))
    phone = forms.CharField(max_length=18, widget=forms.TextInput(attrs={"placeholder": "+7 (777) 777-7777"}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={"placeholder": "Email"}))

    validator: UserValidatorInterface = get_user_validator()

    def clean_phone(self) -> str:
        phone = self.cleaned_data["phone"]
        phone = self.validator.get_raw_phone(phone)

        if not self.validator.is_valid_phone(phone):
            self.add_error("phone", UserErrorsMessages.incorrect_phone)

        return phone


class LoginForm(forms.Form):
    phone_or_email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Email или телефон"}))
    password = forms.CharField(
        max_length=18, widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "autocomplete": "off"})
    )

    validator: UserValidatorInterface = get_user_validator()

    def clean_phone_or_email(self) -> str:
        phone_or_email = self.cleaned_data["phone_or_email"]
        phone_or_email = self.validator.validate_phone_or_email(phone_or_email)

        if phone_or_email is None:
            self.add_error("phone_or_email", UserErrorsMessages.incorrect_login)

        return phone_or_email


class SetPasswordForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}))
    repeat_password = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"placeholder": "Повтор пароля"})
    )


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Ваш email или телефон"}),
        error_messages={"invalid": "Введите корректный email"},
    )


class AddIdeaForm(forms.Form):
    title = forms.CharField(max_length=60)
    description = forms.CharField(max_length=1000)
    category = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].error_messages = {"required": "Выберите категорию замечания или предложения"}
        self.fields["title"].error_messages = {
            "required": "Сформулируйте тему предложения",
            "max_length": f"Не более {self.fields['title'].max_length} символов с пробелами",
        }
        self.fields["description"].error_messages = {
            "required": "Опишите суть проблемы или идеи",
            "max_length": f"Не более {self.fields['description'].max_length} символов с пробелами",
        }
