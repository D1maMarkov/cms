from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime

from domain.common.screen import ScreenInterface
from domain.user.entities import UserInterface


@dataclass
class IdeaInterface:
    id: int
    user: UserInterface
    category: str

    status: str
    finishe_date: datetime | str

    title: str
    description: str
    admin_answer: str

    user_id: int
    screens = Iterable[ScreenInterface]
