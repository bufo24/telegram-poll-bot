from VoteMemeBot.Models.vote import Vote
from VoteMemeBot.Repository.VoteRepository.vote_repository import VoteRepository
from VoteMemeBot.Repository.unit_of_work import UnitOfWork
from VoteMemeBot.Models.meme import Meme
from VoteMemeBot.Exceptions.meme_exceptions import *


class VoteMemeService:
    def __init__(self):
        self.unit_of_work = UnitOfWork()

    def add_votes(self, user_id, votes: list):
        # Check if memes are valid
        for i in votes:
            meme = Meme(i)
            if (meme.is_valid() is False):
                raise InvalidMemeId
        # Add votes
        self.add_vote(user_id, votes[0], 5)
        self.add_vote(user_id, votes[1], 3)
        self.add_vote(user_id, votes[2], 1)

    def add_vote(self, user_id, meme_id, points):
        print("add vote for user %d meme %d points %d" % (user_id, meme_id, points))
        vote = Vote(user_id, meme_id, points)
        self.unit_of_work.get_vote_repository().add(vote)
        self.unit_of_work.complete()
