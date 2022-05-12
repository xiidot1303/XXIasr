from django.db.models.base import ModelState
from telegram import Bot
from telegram.ext import Dispatcher, ConversationHandler, PicklePersistence
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from dotenv import load_dotenv
import os
from data.config import BOT_TOKEN, ENVIRONMENT
import requests

from bot.main import *
from bot.login import *
from bot.conversationList import *
from bot.settings import *
from bot.cabinet import *
from bot.services import *

bot_obj = Bot(BOT_TOKEN)
persistence = PicklePersistence(filename='persistencebot')

if ENVIRONMENT != 'local': # in production
    updater = 1213
    dp = Dispatcher(bot_obj, None, workers=0, use_context=True, persistence=persistence)
else: # in local computer
    updater = Updater(token=BOT_TOKEN, use_context=True, persistence=persistence)
    dp = updater.dispatcher


login_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states = {
        SELECT_LANG: [MessageHandler(Filters.text(['UZ 🇺🇿', 'RU 🇷🇺']), select_lang)],
        SEND_NAME: [MessageHandler(Filters.text, send_name)],
        SEND_CONTACT: [MessageHandler(Filters.all, send_contact)],
    },
    fallbacks= [],
    name='login',
    persistent=True,
)

settings_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text(lang_dict['settings']), settings)],
    states = {
        ALL_SETTINGS: [MessageHandler(Filters.text, all_settings)],
        LANG_SETTINGS: [CallbackQueryHandler(lang_settings), CommandHandler('start', lang_settings)],
        PHONE_SETTINGS: [MessageHandler(Filters.all, phone_settings)],
        NAME_SETTINGS: [MessageHandler(Filters.text, name_settings)],
    }, 
    fallbacks=[],
    name='settings',
    persistent=True,
)

cabinet_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text(lang_dict['cabinet']), cabinet)],
    states = {
        GET_LOGIN: [MessageHandler(Filters.text, get_login)],
        GET_PASSWORD: [MessageHandler(Filters.text, get_password)],
        MY_CABINET: [MessageHandler(Filters.text, my_cabinet)],
    },
    fallbacks=[],
    name='cabinet',
    persistent=True
)

services_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text(lang_dict['our services']), our_services)],
    states = {
        GET_SERVICE: [MessageHandler(Filters.text, get_services)],
    },
    fallbacks=[],
    name='services',
    persistent=True,
)


dp.add_handler(MessageHandler(Filters.text(lang_dict['contacts']), contacts))
dp.add_handler(MessageHandler(Filters.text(lang_dict['address']), address))


dp.add_handler(services_handler)
dp.add_handler(cabinet_handler)
dp.add_handler(settings_handler)
dp.add_handler(login_handler)
