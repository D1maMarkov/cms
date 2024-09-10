from user.exceptions import IdeaNotFound
from user.idea_repository.repository_interface import IdeaRepositoryInterface
from user.interfaces import UserInterface


class DeleteIdea:
    def __init__(self, repository: IdeaRepositoryInterface):
        self.repository = repository

    def __call__(self, idea_id: int, user: UserInterface) -> None:
        idea = self.repository.get_idea(idea_id)
        if user != idea.user:
            raise IdeaNotFound(f'No idea with id "{idea_id}" written by {user}')

        self.repository.delete_idea(idea.id)