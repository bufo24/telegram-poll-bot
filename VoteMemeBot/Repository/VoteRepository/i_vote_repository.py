from VoteMemeBot.Models.vote import Vote
from VoteMemeBot.Repository.repository import Repository


class IVoteRepository(Repository[Vote]):
    def find_votes_by_userid(self, userid: int) -> list[Vote]:
        raise NotImplementedError
