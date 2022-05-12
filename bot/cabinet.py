from base.models import *
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot.conversationList import *
from telegram.ext import ConversationHandler
from utils.bot import *
from utils.deco import *

@is_start
def get_login(update, context):
    msg = update.message.text
    if msg == get_word('back', update):
        main_menu(update, context)
        return ConversationHandler.END
    
    try:
        client = Client.objects.get(bot_login=msg)
        user = get_user_by_update(update)
        user.login = msg
        user.save()
        update.message.reply_text(get_word('type password', update))
        return GET_PASSWORD
    except Exception as error:
        print(error)
        update.message.reply_text(get_word('incorrect login', update))
        return GET_LOGIN

@is_start
def get_password(update, context):
    msg = update.message.text
    if msg == get_word('back', update):
        update.message.reply_text(get_word('type login', update))
        return GET_LOGIN
    
    user = get_user_by_update(update)
    client = Client.objects.get(bot_login=user.login)
    if msg == client.bot_password:
        user.password = msg
        user.save()
        client.bot_user = user
        client.save()
        make_my_cabinet(update, context)
        return MY_CABINET
        
    else:
        update.message.reply_text(get_word('incorrect password', update))
        return GET_PASSWORD

@check_authorized
def my_cabinet(update, context):
    msg = update.message.text
    bot = context.bot

    if msg == get_word('exit', update):
        user = get_user_by_update(update)
        user.login = ''
        user.password = ''
        user.save()
        client = Client.objects.get(bot_user = user)
        client.bot_user = None
        client.save()
        update.message.reply_text(get_word('you are logged out', update))
        main_menu(update, context)
        return ConversationHandler.END
