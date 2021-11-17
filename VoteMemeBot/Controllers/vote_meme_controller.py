from VoteMemeBot.Services.vote_meme_service import VoteMemeService


class VoteMemeController:
    def __init__(self):
        self.vote__meme_service = VoteMemeService()

    def add_votes(self, user_id, votes):
        self.vote__meme_service.add_votes(user_id, votes)
