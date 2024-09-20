from domain.user.exceptions import IdeaNotFound
from domain.user.idea_repository_interface import IdeaRepositoryInterface
from domain.user.referral import UserInterface


class RemoveLike:
    def __init__(self, repository: IdeaRepositoryInterface):
        self.repository = repository

    def __call__(self, idea_id: int, user: UserInterface) -> None:
        idea = self.repository.get_idea(idea_id)

        if not idea:
            raise IdeaNotFound(f'no idea with id "{idea_id}"')

        self.repository.delete_like(user.id, idea_id)
