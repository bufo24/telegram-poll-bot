from MemeVoteBot.Models.vote import Vote
from MemeVoteBot.Repository.repository import Repository


class IVoteRepository(Repository[Vote]):
    def find_votes_by_userid(self, userid: int) -> list[Vote]:
        raise NotImplementedError

    def get_all_points(self) -> list:
        raise NotImplementedError
