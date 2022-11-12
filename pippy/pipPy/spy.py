from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
import datetime


def log(update: Update, context: ContextTypes):
    time = datetime.datetime.now().strftime('%d.%m.%y || %H:%M')
    file = open('db.csv', 'a')
    file.write(f'{time} || {update.effective_user.id} || {update.effective_user.first_name} || {update.message.text}\n')
    file.close()

