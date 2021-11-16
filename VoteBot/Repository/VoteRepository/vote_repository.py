from VoteBot.Exceptions.database_exceptions import NoResult
from VoteBot.Models.vote import Vote
from VoteBot.Repository.VoteRepository.i_vote_repository import IVoteRepository


class VoteRepository(IVoteRepository):

    def __init__(self, database):
        self.Model = Vote
        super().__init__(database)

    def find_votes_by_userid(self, userid: int) -> list[Vote]:
        result: list[Vote] = self.build() \
            .filter(Vote.user_id == userid) \
            .all()
        if not result:
            raise NoResult("No votes for this userid")
        return result