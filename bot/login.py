from base.models import *
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot.conversationList import *
from telegram.ext import ConversationHandler
from utils.bot import *
from utils.deco import *

@is_start_registr
def select_lang(update, context):
    text = update.message.text
    if 'UZ' in text:
        Bot_user.objects.get_or_create(user_id=update.message.chat.id)
        obj = Bot_user.objects.get(user_id=update.message.chat.id)
        obj.lang = 'uz'
        obj.save()
        update.message.reply_text(get_word('type name', update), reply_markup=ReplyKeyboardMarkup([[get_word('back', update)]], resize_keyboard=True))
        return SEND_NAME
    elif 'RU' in text:
        Bot_user.objects.get_or_create(user_id=update.message.chat.id)
        obj = Bot_user.objects.get(user_id=update.message.chat.id)
        obj.lang = 'ru'
        obj.save()
        update.message.reply_text(get_word('type name', update), reply_markup=ReplyKeyboardMarkup([[get_word('back', update)]], resize_keyboard=True))
        return SEND_NAME
    else:
        update.message.reply_text('Bot tilini tanlang\n\nВыберите язык бота', reply_markup=ReplyKeyboardMarkup(keyboard=[['UZ 🇺🇿', 'RU 🇷🇺']], resize_keyboard=True))


@is_start_registr
def send_name(update, context):
    if update.message.text == get_word('back', update):
        update.message.reply_text('Bot tilini tanlang\n\nВыберите язык бота', reply_markup=ReplyKeyboardMarkup(keyboard=[['UZ 🇺🇿', 'RU 🇷🇺']], resize_keyboard=True))
        return SELECT_LANG

    obj = Bot_user.objects.get(user_id=update.message.chat.id)
    obj.name=update.message.text
    obj.username=update.message.chat.username
    obj.firstname = update.message.chat.first_name
    obj.save()
    i_contact = KeyboardButton(text=get_word('leave number', update), request_contact=True)
    update.message.reply_text(get_word('send number', update), reply_markup=ReplyKeyboardMarkup([[i_contact], [get_word('back', update)]], resize_keyboard=True))
    return SEND_CONTACT

@is_start_registr
def send_contact(update, context):
    if update.message.text == get_word('back', update):
        update.message.reply_text(get_word('type name', update), reply_markup=ReplyKeyboardMarkup([[get_word('back', update)]], resize_keyboard=True))
        return SEND_NAME

    if update.message.contact == None or not update.message.contact:
        phone_number = update.message.text
    else:
        phone_number = update.message.contact.phone_number
    # check that phone is available or no
    is_available = Bot_user.objects.filter(phone=phone_number).exclude(user_id=update.message.chat.id)
    if is_available:
        update.message.reply_text(get_word('number is logged',update))
        return SEND_CONTACT
    obj = Bot_user.objects.get(user_id=update.message.chat.id)
    obj.phone = phone_number
    obj.save()
    main_menu(update, context)
    return ConversationHandler.END
