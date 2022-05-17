from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import InputMediaVideo, InputMediaPhoto
from telegram.ext import ConversationHandler

from base.models import *
from bot.conversationList import *
from utils.bot import *
from utils.deco import *
from control.settings import BASE_DIR
from bot.uz_ru import lang_dict

@is_start
def get_services(update, context):
    bot = context.bot
    msg = update.message.text

    if msg == get_word('car number', update):
        text='car number' 
        file=['car_number', 'car_number2']
    
    elif msg == get_word('tonirovka', update):
        text='tonirovka' 
        file=['tonirovka']
    
    elif msg == get_word('auction', update):
        text='auction' 
        file=['auction']
    
    elif msg == get_word('yagona darcha', update):
        text='yagona darcha' 
        file=['yagona_darcha', 'yagona_darcha2']
    
    elif msg == get_word('accounting', update):
        text='accounting' 
        file=['BAACAgIAAxkBAAIKGWKDnTXZpQggyE9DiYfmBPbDofl1AAI0GQACLDkYSMWGcDHxYxtdJAQ']
        # file=['accounting']
    
    elif msg == get_word('kochmas mulk', update):
        text='kochmas mulk' 
        file=['kochmas_mulk', 'kochmas_mulk2']
    
    elif msg == get_word('stamp', update):
        text='stamp' 
        file=['BAACAgIAAxkBAAIKF2KDl-xeD0Tj5OIprgbgjCk_eBGZAAMZAAIsORhICfgn0j_Nj8ckBA']
        # file=['stamp']
    
    # elif msg == get_word('', update):
    #     text='' 
    #     file=['']
    
    send_service(update=update, context=context, text=text, files=file)
