from MemeVoteBot.Controllers.meme_vote_controller import MemeVoteController
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

from config import token


class MemeVoteBot:

    def __init__(self):
        self.meme_vote_controller = MemeVoteController()
        self.updater = Updater(token)
        self.__start_handlers()
        self.updater.start_polling()
        self.updater.idle()

    def __start_handlers(self):
        self.updater.dispatcher.add_handler(CommandHandler('vote', self.vote_command))
        self.updater.dispatcher.add_handler(CommandHandler('votes', self.votes_command))

    # /vote 10 22 14
    # where the numbers are the meme IDs
    def vote_command(self, update: Update, context: CallbackContext) -> list:
        message = update.message.text.removeprefix("/vote ")
        user_id = update.message.from_user.id
        args = message.split(" ")

        explanation_text = "Please vote for exactly three memes! e.g. '/vote 1 2 3' where meme 1 gets 5 points, meme 2 gets 3 points and meme 3 gets 1 points"
        # Parse args
        if (len(args) == 0):
            update.message.reply_text("No votes found.")
        elif (len(args) != 3):
            update.message.reply_text(explanation_text)
        else:
            try:
                votes = [int(i) for i in args]
                self.meme_vote_controller.add_votes(user_id, votes)
            except Exception as e:
                update.message.reply_text(explanation_text)
                return
            update.message.reply_text("Votes submitted!")

    def votes_command(self, update: Update, context: CallbackContext) -> list:
        try:
            tuples = self.meme_vote_controller.get_all_points()
            msg = ""
            for tuple in tuples:
                msg = msg + "Meme ID: " + str(tuple[0]) + \
                    " has " + str(tuple[1]) + " points\n"
            update.message.reply_text(msg)
        except Exception as e:
            update.message.reply_text(str(e))
