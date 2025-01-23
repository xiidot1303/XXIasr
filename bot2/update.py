from django.db.models.base import ModelState
from telegram import Bot
from telegram.ext import Dispatcher, ConversationHandler, PicklePersistence
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from data.config import BOT_TOKEN, ENVIRONMENT

from bot2.main import *
from bot2.conversationList import *

bot_obj = Bot(BOT_TOKEN)
persistence = PicklePersistence(filename='persistencebot2')

if ENVIRONMENT != 'local': # in production
    updater = 1213
    dp = Dispatcher(bot_obj, None, workers=0, use_context=True, persistence=persistence)
else: # in local computer
    updater = Updater(token=BOT_TOKEN, use_context=True, persistence=persistence)
    dp = updater.dispatcher


start_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        GET_CONTACT: [MessageHandler(Filters.contact, get_contact)],
        GET_SERVICE: [MessageHandler(Filters.text & ~Filters.command, get_service)],

    },
    fallbacks=[
        CommandHandler('start', start)
    ],
    name='start',
    persistent=True
)

dp.add_handler(start_handler)