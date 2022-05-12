from telegram import ReplyKeyboardMarkup, KeyboardButton
import telegram
from bot.uz_ru import lang_dict
from base.models import *
from telegram.ext import ConversationHandler
from datetime import date, datetime
from bot.conversationList import *
from utils.bot import *

def is_start_registr(func):
    def func_arguments(*args, **kwargs):
        bot = args[1].bot
        try:
            lalal = args[0].message.text
            update = args[0]
            data = ''
        except:
           update = args[0].callback_query
           data = update.data  
        id = update.message.chat.id
        if update.message.text == '/start':
            update.message.reply_text('🤖 Xush kelibsiz!\n Bot tilini tanlang  🌎 \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\n 👋 Добро пожаловать \n \U0001F1FA\U0001F1FF Выберите язык бота \U0001F1F7\U0001F1FA', reply_markup=ReplyKeyboardMarkup(keyboard=[['UZ 🇺🇿', 'RU 🇷🇺']], resize_keyboard=True))
            return SELECT_LANG

 
        else:
            return func(*args, **kwargs)
    return func_arguments



def is_start(func):    # This deco break registration if user send /start.
    def func_arguments(*args, **kwargs):
        bot = args[1].bot
        try:
            lalal = args[0].message.text
            update = args[0]
            data = ''
        except:
           update = args[0].callback_query
           data = update.data  
        id = update.message.chat.id
        if update.message.text == '/start' or data == 'main_menu' or update.message.text == get_word('main menu', update):
            user = get_user_by_update(update)
            # task
            main_menu(args[0], args[1])
            return ConversationHandler.END
        else:
            return func(*args, **kwargs)
    return func_arguments

def check_authorized(func):
    def func_arguments(*args, **kwargs):
        bot = args[1].bot
        try:
            lalal = args[0].message.text
            update = args[0]
            data = ''
        except:
           update = args[0].callback_query
           data = update.data  
        id = update.message.chat.id
        user = get_user_by_update(update)
        if update.message.text == '/start' or data == 'main_menu' or update.message.text == get_word('main menu', update):
            main_menu(args[0], args[1])
            return ConversationHandler.END
        elif not is_authorized(update):
            if Client.objects.filter(bot_user = user):

                # remove bot user from client
                client = Client.objects.get(bot_user = user)
                client.bot_user = None
                client.save()
                bot.send_message(update.message.chat.id, get_word('login or password is changed', update))
            # erase login and password from bot user
            user.login = ''
            user.password = ''
            user.save()
            main_menu(args[0], args[1])
            return ConversationHandler.END

        else:
            return func(*args, **kwargs)
    return func_arguments