from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.common.screen import ImageInterface
from domain.domains.domain import DomainInterface


@dataclass
class UserInterface:
    pk: int
    id: int
    username: str
    second_name: str
    full_name: str

    phone: str
    phone_is_confirmed: bool

    email: str
    new_email: str
    email_is_confirmed: bool

    password: str | None

    site: Optional["SiteInterface"] | None

    register_on_site: Optional["SiteInterface"] | None
    register_on_domain: DomainInterface | None

    is_superuser: bool
    profile_picture: str
    test: bool

    def check_password(self, password: str):
        pass

    def set_password(self, password: str):
        pass

    def confirm_email(self) -> None:
        pass


@dataclass
class SiteInterface:
    id: int
    domain: DomainInterface

    created_at: datetime | None = None
    name: str | None = None
    owner: str | None = None
    contact_info: str | None = None
    user: Optional["UserInterface"] = None

    advertising_channel: str | None = None
    use_default_settings: bool | None = None
    is_active: bool | None = None
    subdomain: str | None = None
    logo: ImageInterface | None = None
    logo2: ImageInterface | None = None
    logo_width: int | None = None
    logo_width_mobile: int | None = None

    font: str | None = None
    font_size: int | None = None

    @property
    def adress(self) -> str:
        if self.subdomain:
            return f"{self.subdomain}.{self.domain.domain}"
        return self.domain.domain

    def activate(self) -> None:
        pass

    def deactivate(self) -> None:
        pass
