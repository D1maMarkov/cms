from enum import Enum


class Errors(str, Enum):
    incorrect_file_name = "Неккоректное название файла"
    block_with_name_already_exist = "Уже есть блок, привязанный к этому имени"
    template_doesnt_exist = "Нет такого html файла"


class UserErrors(str, Enum):
    username_with_phone_alredy_exists = "Пользователь с таким телефоном уже существует"
    username_with_email_alredy_exists = "Пользователь с такой почтой уже существует"
    incorrect_phone = "Неверный номер телефона"
