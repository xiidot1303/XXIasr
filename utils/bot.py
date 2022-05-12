from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import telegram
from bot.uz_ru import lang_dict
from base.models import *
from telegram.ext import ConversationHandler
from datetime import date, datetime
from bot.conversationList import *
from telegram import InputMediaVideo, InputMediaPhoto
from control.settings import BASE_DIR

def main_menu(update, context):
    try:
        a = update.callback_query.id
        update = update.callback_query
    except:
        www= 0 # do nothing
    
    bot = context.bot
    keyboard=[[get_word('cabinet', update)], [get_word('our services', update)], [get_word('address', update)], 
        [get_word('contacts', update)], [get_word('settings', update)]]
    bot.send_message(update.message.chat.id, get_word('main menu', update), reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))
    check_username(update)

    
def make_button_settings(update, context):
    try:
        a = update.callback_query.id
        update = update.callback_query
    except:
        www= 0 # do nothing
    bot = context.bot
    keyboard=[[get_word('change lang', update)], [get_word('change name', update)], [get_word('change phone number', update)], [get_word('main menu', update)]]
    bot.send_message(update.message.chat.id, get_word('settings desc', update), reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))


def make_my_cabinet(update, context):
    try:
        a = update.callback_query.id
        update = update.callback_query
    except:
        www= 0 # do nothing
    bot = context.bot
    keyboard = [[get_word('main menu', update)], [get_word('exit', update)]]
    bot.send_message(update.message.chat.id, get_word('cabinet', update), reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def get_word(text, update):
    user = Bot_user.objects.get(user_id=update.message.chat.id)
    if user.lang == 'uz':
        return lang_dict[text][0]
    else:
       return lang_dict[text][1]

def is_registered(id):
    if Bot_user.objects.filter(user_id=id):
        return True
    else:
        return False

def is_authorized(update):
    id  = update.message.chat.id
    if Client.objects.filter(bot_user__user_id = id):
        # client = Client.objects.get(bot_user__user_id=id)
        # user = get_user_by_update(update)
        # if client.bot_login == user.login and client.bot_password == user.password:
        #     return True
        # else:
        #     return False
        return True
    else:
        return False

def get_user_by_update(update):
    user = Bot_user.objects.get(user_id=update.message.chat.id)
    return user

def check_username(update):
    user = get_user_by_update(update)
    
    if user.username != update.message.chat.username:
        user.username = update.message.chat.username
        user.save()
    if user.firstname != update.message.chat.first_name:
        user.firstname = update.message.chat.first_name
        user.save()
    

def get_variants_for_buttons(text):
    l = list(str(text).split('//'))
    try:
        l.remove('')
    except:
        ok = True
    r_list = [[i] for i in l]
    return r_list

def split_by_slash(text):
    l = list(str(text).split('//'))
    try:
        l.remove('')
    except:
        ok = True
    return l

def compress_by_slash(l):
    text_ = ''
    for i in l:
        text_ += i+'//'
    return text_


def send_service(update, context, text, files):
    bot = context.bot
    media_group = []
    for f in files:
        video = open(str(BASE_DIR) + '/static/videos/{}.mp4'.format(f), 'rb')
        media_group.append(InputMediaVideo(video))
    bot.send_message(update.message.chat.id, get_word('watch video below', update))
    bot.send_media_group(chat_id = update.message.chat.id, media = media_group)