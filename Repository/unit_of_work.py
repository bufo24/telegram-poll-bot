import config
from Repository.VoteRepository.vote_repository import VoteRepository
from Repository.VoteRepository.i_vote_repository import IVoteRepository
from Repository.database import Database
from Repository.i_repository import IRepository
from Repository.i_unit_of_work import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    def __init__(self,
                 database_uri=config.DbConfig.SQLALCHEMY_DATABASE_URI,
                 vote_repository: IRepository = None):
        self.database = Database(database_uri)
        self.session = self.database.session()
        # repositories
        self.vote_repository = vote_repository
        if not self.vote_repository:
            self.vote_repository = VoteRepository(self.session)

    def get_vote_repository(self) -> IVoteRepository:
        return self.vote_repository

    def set_vote_repository(self, repository: IRepository) -> None:
        self.vote_repository = repository

    def complete(self) -> None:
        self.session.commit()
