from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import InputMediaVideo, InputMediaPhoto
from telegram.ext import ConversationHandler

from base.models import *
from bot.conversationList import SELECT_LANG
from utils.bot import *
from control.settings import BASE_DIR

def start(update, context):
    
    if is_registered(update.message.chat.id):
        main_menu(update, context)
    else:
        hello_text = '🤖 Xush kelibsiz!\n Bot tilini tanlang  🌎 \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\n 👋 Добро пожаловать \n \U0001F1FA\U0001F1FF Выберите язык бота \U0001F1F7\U0001F1FA'
        update.message.reply_text(hello_text, reply_markup=ReplyKeyboardMarkup(keyboard=[['UZ 🇺🇿', 'RU 🇷🇺']], resize_keyboard=True))
        return SELECT_LANG


def settings(update, context):
    make_button_settings(update, context)
    return ALL_SETTINGS

def cabinet(update, context):
    if is_authorized(update):
        make_my_cabinet(update, context)
        return MY_CABINET
    else:
        update.message.reply_text(get_word('type login', update), reply_markup = 
            ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True))
        return GET_LOGIN

def address(update, context):
    bot = context.bot
    bot.send_message(update.message.chat.id, get_word('all addresses', update), parse_mode = telegram.ParseMode.HTML)

    bot.send_message(update.message.chat.id, get_word('1st office', update), parse_mode = telegram.ParseMode.HTML)
    bot.send_location(update.message.chat.id, 39.4287332, 67.2386705)
    
    bot.send_message(update.message.chat.id, get_word('2nd office', update), parse_mode = telegram.ParseMode.HTML)
    bot.send_location(update.message.chat.id, 39.4178555, 67.2393289)
    
    
    bot.send_message(update.message.chat.id, get_word('3rd office', update), parse_mode = telegram.ParseMode.HTML)
    bot.send_location(update.message.chat.id, 39.4259444, 67.2368611)

def our_services(update, context):
    bot = context.bot
    keyboard_words = ['accounting', 'car number', 'tonirovka', 'yagona darcha', 'auction', 'kochmas mulk', 'stamp', 'main menu']
    keyboard = [[get_word(i, update)] for i in keyboard_words]
    bot.send_message(update.message.chat.id, get_word('our all services', update), reply_markup = 
        ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

    # video = open(str(BASE_DIR) + '/static/videos/auksion.mp4', 'rb')
    video = 'BAACAgIAAxkBAAINrmKwe0UuXOrSVg-aUwewehgTe6SPAAJFGQACLDkYSGz8o9CUmhhbKAQ'
    # video = 'AAMCAgADGQEAAg2uYrB7RS5c6tJWD5pTB7B6GBN7pI8AAkUZAAIsORhIbPyj0JSaGFsBAAdtAAMoBA'
    bot.send_video(chat_id = update.message.chat.id, video=video)
    return GET_SERVICE


def contacts(update, context):
    main_office = '<b>{}</b>: +998557012100'.format(get_word('main office', update))
    car_number = '<b>{}</b>: +998992231118'.format(get_word('car number', update))
    cadastre = '<b>{}</b>: +998992231115'.format(get_word('cadastre', update))
    pc_service = '<b>{}</b>: +998901962266'.format(get_word('pc service', update))
    msg = '{}\n\n{}\n\n{}\n\n{}'.format(main_office, car_number, cadastre, pc_service)
    update.message.reply_text(msg, parse_mode=telegram.ParseMode.HTML)

def send_video_id(update, context):
    update.message.reply_text(update.message.video.file_id)