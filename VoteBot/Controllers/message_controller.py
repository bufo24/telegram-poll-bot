from VoteBot.Services.vote_service import VoteService

class MessageController:

    def __init__(self):
        self.vote_service = VoteService()

    def add_votes(self, user_id, votes):
        self.vote_service.add_votes(user_id, votes)