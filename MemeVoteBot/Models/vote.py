from sqlalchemy import Column, Integer

from MemeVoteBot.Repository.database import Base


class Vote(Base):
    __tablename__ = 'votes'
    vote_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    meme_id = Column(Integer)
    points = Column(Integer)

    def __init__(self, user_id, meme_id, points: int):
        self.user_id = user_id
        self.meme_id = meme_id
        self.points = points
