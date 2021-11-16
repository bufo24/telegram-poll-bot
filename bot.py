from sqlalchemy.sql.functions import user
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from Models.vote import Vote
from config import token
from Repository.i_unit_of_work import IUnitOfWork
from Repository.unit_of_work import UnitOfWork

def is_valid_meme(meme_id) -> bool:
    if (meme_id < 150):
        return True
    return False

def add_vote(user_id, meme_id, points):
    print("add vote for user %d meme %d points %d" % (user_id, meme_id, points))
    vote = Vote(user_id, meme_id, points)
    unit_of_work.get_vote_repository().add(vote)
    unit_of_work.complete()

# /vote 10 22 14
# where the numbers are the meme IDs
def vote_command(update: Update, context: CallbackContext) -> list:
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
            # Check if memes are valid
            for i in votes:
                if (is_valid_meme(i) == False):
                    update.message.reply_text("Invalid meme! %s" % explanation_text)
                    return
            # Add votes
            add_vote(user_id, votes[0], 5)
            add_vote(user_id, votes[1], 3)
            add_vote(user_id, votes[2], 1)
        except:
            update.message.reply_text(explanation_text)

unit_of_work: IUnitOfWork = UnitOfWork()
updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('vote', vote_command))

updater.start_polling()
updater.idle()