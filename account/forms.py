from django import forms
from PIL import Image

from utils.errors import Errors
from utils.format_phone import get_raw_phone
from utils.validators import is_valid_email, is_valid_phone


class ChangeSiteForm(forms.Form):
    site = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    font = forms.IntegerField()
    font_size = forms.IntegerField()
    logo = forms.FileField(required=False)
    logo_size = forms.IntegerField(required=False)
    owner = forms.CharField(max_length=200)
    contact_info = forms.CharField(max_length=200)
    delete_logo = forms.CharField(max_length=10)
    # socials = forms.CharField(max_length=5000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["site"].error_messages = {"required": "Укажите адрес своего сайта"}
        self.fields["name"].error_messages = {"required": "Это поле обязательное"}
        self.fields["font"].error_messages = {"required": "Это поле обязательное"}
        self.fields["font_size"].error_messages = {"required": "Это поле обязательное"}
        self.fields["owner"].error_messages = {"required": "Укажите свое имя или название организации"}
        self.fields["contact_info"].error_messages = {"required": "Укажите свой емейл, телефон или другой способ связи"}

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not (4 <= len(name) <= 16):
            self.add_error("name", "Название от 4 до 16 символов")

        return name

    def clean_site(self):
        site = self.cleaned_data["site"]
        if len(site) < 4:
            self.add_error("site", "Длина адреса не менее 4 символов")

        if not (site.isalnum() and all(c.isascii() for c in site)):
            self.add_error("site", "Можно использовать только латинские буквы и цифры")

        return site

    def clean_logo(self):
        logo = self.cleaned_data["logo"]
        if logo:
            if logo.size > 102400:
                self.add_error("logo", Errors.to_large_file.value)

            file_extension = logo.name.split(".")[-1].lower()
            if file_extension not in ["png", "gif"]:
                self.add_error("logo", Errors.wrong_image_format.value)

            try:
                img = Image.open(logo)
                width, height = img.size
                if height > 200 or width > 500:
                    self.add_error("logo", Errors.to_large_image_size.value)
            except Exception as e:
                pass

        return logo


class ChangeUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    second_name = forms.CharField(max_length=200)

    email = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=18)
    social_network = forms.CharField(required=False)
    adress = forms.CharField(required=False)

    profile_picture = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].error_messages = {"required": "Укажите свое имя"}
        self.fields["second_name"].error_messages = {"required": "Укажите свою фамилию"}
        self.fields["email"].error_messages = {"required": "Это поле обязательное"}
        self.fields["phone"].error_messages = {"required": "Это поле обязательное"}

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if not is_valid_phone(phone):
            self.add_error("phone", "Укажите корректный телефон")

        return get_raw_phone(phone)

    def clean_email(self):
        email = self.cleaned_data["email"]

        if not is_valid_email(email):
            self.add_error("email", "Введите корректный email")

        return email


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    repeat_password = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["current_password"].error_messages = {"required": "Это поле обязательное"}
        self.fields["password"].error_messages = {"required": "Это поле обязательное"}
        self.fields["repeat_password"].error_messages = {"required": "Это поле обязательное"}

    def clean_password(self):
        password = self.cleaned_data["password"]

        if len(password) < 6:
            self.add_error("password", "Минимум 6 латинских букв и цифр")

        return password
