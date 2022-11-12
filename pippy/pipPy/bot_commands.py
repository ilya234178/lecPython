from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
import datetime
from spy import *

def hi_command(update: Update, context: ContextTypes):
    log(update, context)
    update.message.reply_text(f'Hi man {update.effective_user.first_name}')

def menu_command(update: Update, context: ContextTypes):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/sub\n/mult\n/div')

def help_command(update: Update, context: ContextTypes):
    log(update, context)
    update.message.reply_text(f'/hi - Приветствие\n/time - Точное время\n/help - Список команд\n/sum - Сложение\n/sub - Вычитание\n/mult - Умножение\n/div- Деление')

def time_command(update: Update, context: ContextTypes):
    log(update, context)
    time = datetime.datetime.now().strftime('%d.%m.%y || %H:%M')
    update.message.reply_text(f'{time}')

def sum_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 1231 
    x = int(items[1])
    y = int(items[2])

    update.message.reply_text(f'{x} + {y} = {x+y}')

def sub_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  
    x = int(items[1])
    y = int(items[2])

    update.message.reply_text(f'{x} - {y} = {x-y}')

def mult_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  
    x = int(items[1])
    y = int(items[2])

    update.message.reply_text(f'{x} * {y} = {x*y}')

def div_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  
    x = int(items[1])
    y = int(items[2])

    update.message.reply_text(f'{x} / {y} = {x/y}')