class Meme:
    meme_id = None

    def __init__(self, meme_id):
        self.meme_id = meme_id

    def is_valid(self) -> bool:
        # Get amount of memes
        if (self.meme_id < 150):
            return True
        return False