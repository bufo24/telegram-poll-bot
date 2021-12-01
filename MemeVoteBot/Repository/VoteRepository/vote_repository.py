from MemeVoteBot.Exceptions.database_exceptions import NoResult
from MemeVoteBot.Models.vote import Vote
from MemeVoteBot.Repository.VoteRepository.i_vote_repository import IVoteRepository
from sqlalchemy import func


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

    def get_all_points(self) -> list:
        result: list[int, int] = self._session.query(
                Vote.meme_id, func.sum(Vote.points)
            ).group_by(Vote.meme_id) \
            .order_by(func.sum(Vote.points).desc()) \
            .all()
        if not result:
            raise NoResult("No votes found")
        return result
