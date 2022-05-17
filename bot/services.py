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
        file=['BAACAgIAAxkBAAIKHGKDnmrrrnhU9OQsqlxBFOKqTGI7AAI_GQACLDkYSAIK4q1PetKcJAQ', 
            'BAACAgIAAxkBAAIKHWKDnprjpk14euiGSuUpiGFx6qOKAAJAGQACLDkYSOx35BFFV70vJAQ']
    
    elif msg == get_word('tonirovka', update):
        text='tonirovka' 
        file=['BAACAgIAAxkBAAIKIWKDn4aCHChgz7TOnpYq9YH767xmAAJIGQACLDkYSBjNWdNX9vTQJAQ']
        # file=['tonirovka']
    
    elif msg == get_word('auction', update):
        text='auction' 
        file=['BAACAgIAAxkBAAIKGmKDngwZPR4gSrg2WDy5oq9p0ccaAAI8GQACLDkYSMqe7V_8JykiJAQ']
        # file=['auction']
    
    elif msg == get_word('yagona darcha', update):
        text='yagona darcha' 
        file=['BAACAgIAAxkBAAIKImKDn7C-7l-eP1Z3pHgNizHgo6_2AAJJGQACLDkYSKNHh_mMYefUJAQ', 
            'BAACAgIAAxkBAAIKI2KDn_A-Cq8maG6gYY_6FlW13XfwAAJLGQACLDkYSDYwsJCIeKsyJAQ']
        # file=['yagona_darcha', 'yagona_darcha2']
    
    elif msg == get_word('accounting', update):
        text='accounting' 
        file=['BAACAgIAAxkBAAIKGWKDnTXZpQggyE9DiYfmBPbDofl1AAI0GQACLDkYSMWGcDHxYxtdJAQ']
        # file=['accounting']
    
    elif msg == get_word('kochmas mulk', update):
        text='kochmas mulk' 
        file=['BAACAgIAAxkBAAIKHmKDntBY7lxR_LE3noB_jz5w5egdAAJCGQACLDkYSGyO9-jQRqjbJAQ', 
            'BAACAgIAAxkBAAIKH2KDnv4Y-JFq5-ZIUK85u3YIpdEHAAJEGQACLDkYSF29VvdVF2w-JAQ']
    
    elif msg == get_word('stamp', update):
        text='stamp' 
        file=['BAACAgIAAxkBAAIKF2KDl-xeD0Tj5OIprgbgjCk_eBGZAAMZAAIsORhICfgn0j_Nj8ckBA']
        # file=['stamp']
    
    # elif msg == get_word('', update):
    #     text='' 
    #     file=['']
    
    send_service(update=update, context=context, text=text, files=file)
