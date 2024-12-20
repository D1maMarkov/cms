from domain.user.notifications.repository import NotificationRepositoryInterface
from infrastructure.persistence.repositories.notification_repository import (
    get_notification_repository,
)


class FormatNotification:
    def __init__(self, notification_repository: NotificationRepositoryInterface) -> None:
        self.notification_repository = notification_repository

    def __call__(self, notification_id: int) -> str:
        notification = self.notification_repository.get(notification_id)

        notification_text = notification.message

        patterns = self.notification_repository.get_patterns(notification_id)

        for pattern in patterns:
            if pattern.method:
                arg = ""
                if pattern.arg:
                    if pattern.arg.isdigit():
                        arg = pattern.arg
                    else:
                        arg = f'''"{pattern.arg}"'''

                string = f"""<a class="ref" onclick="{pattern.method}({arg})">{pattern.text}</a>"""
            else:
                string = pattern.text

            notification_text = notification_text.replace(pattern.tag, string)

        return notification_text


def get_format_notification(
    notifications_repository: NotificationRepositoryInterface = get_notification_repository(),
) -> FormatNotification:
    return FormatNotification(notification_repository=notifications_repository)
