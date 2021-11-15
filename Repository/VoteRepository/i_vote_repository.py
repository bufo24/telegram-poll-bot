from Models.vote import Vote
from Repository.repository import Repository

class IVoteRepository(Repository[Vote]):
    def find_votes_by_userid(self, userid: int) -> Vote:
        raise NotImplementedError
