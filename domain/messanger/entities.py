from dataclasses import dataclass

from domain.user.user import UserInterface


@dataclass
class ChatInterface:
    id: int


@dataclass
class ChatUserInterface:
    id: int
    user: UserInterface
    chat: ChatInterface
