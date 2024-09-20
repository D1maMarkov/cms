import traceback

from django.utils.deprecation import MiddlewareMixin

from infrastructure.email_services.work_email_service.email_service import (
    get_work_email_service,
)
from infrastructure.get_ip import get_client_ip
from infrastructure.logging.errors import ErrorLogger
from infrastructure.persistence.repositories.errors_repository import (
    get_errors_repository,
)
from infrastructure.persistence.repositories.system_repository import (
    get_system_repository,
)


class ExceptionLoggingMiddleware(MiddlewareMixin):
    logger = ErrorLogger(get_errors_repository(), get_system_repository(), get_work_email_service())

    def process_exception(self, request, exception):
        error_message = traceback.format_exc()

        user = request.user if request.user.is_authenticated else None

        self.logger(
            message=error_message, client_ip=get_client_ip(request), path=request.build_absolute_uri(), user=user
        )

        return None
