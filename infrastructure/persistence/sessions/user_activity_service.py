from django.utils.timezone import now

from application.sessions.dto import UserActivityDTO


class UserActivitySessionService:
    def __init__(self, request_service, user_session_repository):
        self.request_service = request_service
        self.user_session_repository = user_session_repository

    def get_initial_data(self, site, user_id, device, utm_source, auth=None):
        ip = self.request_service.get_client_ip()
        hacking = False
        hacking_reason = None
        if not auth:
            auth = "login" if user_id else None

        user_session_data = UserActivityDTO(
            ip=ip,
            start_time=now().isoformat(),
            end_time=now().isoformat(),
            site=site,
            device=device,
            user_id=user_id,
            utm_source=utm_source,
            hacking=hacking,
            hacking_reason=hacking_reason,
            auth=auth,
        )

        return user_session_data
