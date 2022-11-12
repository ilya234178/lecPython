# from isOdd import isOdd


# print(isOdd(1)) 
# print(isOdd(4)) 


# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))


# import matplotlib.pyplot as plt
# # import numpy as np

# list = [1, 4, 3, 2, 7, 11, 26]
# plt.plot(list)

# plt.show()

from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
from bot_commands import *




updater = Updater("5561859694:AAGQDXezQzFWfZ3bbzbQrpe1ntrxMoAkASg")

updater.dispatcher.add_handler(CommandHandler("hello", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("menu", menu_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))
updater.dispatcher.add_handler(CommandHandler("sub", sub_command))
updater.dispatcher.add_handler(CommandHandler("mult", mult_command))
updater.dispatcher.add_handler(CommandHandler("div", div_command))

print('server start')
updater.start_polling()
updater.idle()