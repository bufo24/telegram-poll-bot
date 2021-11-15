from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from Models.vote import Vote
from config import token

def vote_command(update: Update, context: CallbackContext) -> list:
    message = update.message.text.removeprefix("/vote ")
    user_id = update.message.from_user.id
    args = message.split(" ")
    if (len(args) == 0):
        update.message.reply_text("No votes found.")

updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('vote', vote_command))

updater.start_polling()
updater.idle()