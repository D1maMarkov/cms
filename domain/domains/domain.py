from dataclasses import dataclass


@dataclass
class DomainInterface:
    domain: str
    is_partners: bool


@dataclass
class SiteInterface:
    domain: DomainInterface

    name: str
    owner: str
    contact_info: str
    created_at: str

    advertising_channel: str = None
    use_default_settings: bool = None
    is_active: bool = None
    subdomain: str = None

    @property
    def adress(self) -> str:
        if self.subdomain:
            return f"{self.subdomain}.{self.domain.domain}"
        return self.domain.domain
