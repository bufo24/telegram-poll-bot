from MemeVoteBot.Services.meme_vote_service import MemeVoteService


class MemeVoteController:
    def __init__(self):
        self.vote__meme_service = MemeVoteService()

    def add_votes(self, user_id, votes):
        self.vote__meme_service.add_votes(user_id, votes)

    def get_all_points(self) -> list:
        return self.vote__meme_service.get_points_per_meme()
