from MemeVoteBot.Services.meme_vote_service import MemeVoteService


class MemeVoteController:
    def __init__(self):
        self.vote__meme_service = MemeVoteService()

    def add_votes(self, user_id, votes):
        self.vote__meme_service.add_votes(user_id, votes)
