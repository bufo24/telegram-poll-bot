from VoteBot.Models.vote import Vote
from VoteBot.Repository.VoteRepository.vote_repository import VoteRepository
from VoteBot.Repository.unit_of_work import UnitOfWork
from VoteBot.Models.meme import Meme
from VoteBot.Exceptions.meme_exceptions import *

class VoteService:

    def __init__(self):
       self.unit_of_work = UnitOfWork()

    def add_votes(self, user_id, votes: list):
        # Check if memes are valid
        for i in votes:
            meme = Meme(i)
            if (meme.is_valid() == False):
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