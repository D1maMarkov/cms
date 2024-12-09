from typing import Any

from application.email_services.work_email_service.email_service_interface import (
    WorkEmailServiceInterface,
)
from application.services.request_service_interface import RequestServiceInterface
from domain.logging.admin import AdminLogRepositoryInterface
from domain.user.user import UserInterface
from infrastructure.email_services.work_email_service.email_service import (
    get_work_email_service,
)
from infrastructure.persistence.repositories.admin_log_repository import (
    get_admin_log_repository,
)


class AdminLoginLogger:
    def __init__(
        self,
        repository: AdminLogRepositoryInterface,
        email_service: WorkEmailServiceInterface,
        request_service: RequestServiceInterface,
    ) -> None:
        self.repository = repository
        self.email_service = email_service
        self.request_service = request_service

    def error(self, fields: dict[str, Any], error: str) -> None:
        ip_address = self.request_service.get_client_ip()

        log = self.repository.create_logg(ip_address, **fields)

        self.email_service.send_error_admin_login_message(ip=ip_address, **fields, time=log.date, error=error)

    def success(self, fields: dict[str, Any]) -> None:
        ip_address = self.request_service.get_client_ip()

        log = self.repository.create_logg(ip_address, **fields)

        self.email_service.send_success_admin_login_message(ip=ip_address, **fields, time=log.date)

    def fake_admin_panel(self, user: UserInterface, **kwargs) -> None:
        ip_address = self.request_service.get_client_ip()
        print(user)
        print(kwargs)

        log = self.repository.create_logg_fake_admin(ip=ip_address, user=user, **kwargs)

        self.email_service.send_fake_admin_login_message(**kwargs, ip=ip_address, user=user, time=log.date)


def get_admin_logger(
    request_service: RequestServiceInterface,
    repository: AdminLogRepositoryInterface = get_admin_log_repository(),
    email_service: WorkEmailServiceInterface = get_work_email_service(),
) -> AdminLoginLogger:
    return AdminLoginLogger(repository=repository, request_service=request_service, email_service=email_service)
