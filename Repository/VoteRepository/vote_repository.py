import datetime

from Exceptions.database_exceptions import NoResult
from Models.vote import Vote
from Repository.VoteRepository.i_vote_repository import IVoteRepository


class VoteRepository(IVoteRepository):

    def __init__(self, database):
        self.Model = Vote
        super().__init__(database)

    def find_votes_by_userid(self, userid: int) -> Vote:
        result: Vote = self.build() \
            .filter(Vote.user_id == userid)
        if not result:
            raise NoResult("No credit at this price")
        return result

