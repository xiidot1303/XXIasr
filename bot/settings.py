from base.models import *
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from bot.conversationList import *
from telegram.ext import ConversationHandler
from utils.bot import *
from utils.deco import *


@is_start
def all_settings(update, context):
    msg = update.message.text
    bot = context.bot
    
    if msg == get_word('change lang', update):
        current_lang = get_user_by_update(update).lang
        if current_lang == 'uz':
            uz_text = 'UZ \U0001F1FA\U0001F1FF   ✅'
            ru_text = 'RU \U0001F1F7\U0001F1FA'
        else:
            uz_text = 'UZ \U0001F1FA\U0001F1FF'
            ru_text = 'RU \U0001F1F7\U0001F1FA    ✅'
        i_uz = InlineKeyboardButton(text=uz_text, callback_data='set_lang_uz')
        i_ru = InlineKeyboardButton(text=ru_text, callback_data='set_lang_ru')
        i_back = InlineKeyboardButton(get_word('back', update), callback_data='back_settings')
        del_msg = update.message.reply_text(get_word('select lang', update), reply_markup=ReplyKeyboardRemove(remove_keyboard=True))
        bot.delete_message(update.message.chat.id, del_msg.message_id)
        bot.send_message(update.message.chat.id, get_word('select lang', update), reply_markup = InlineKeyboardMarkup([[i_uz], [i_ru], [i_back]]))
        return LANG_SETTINGS

    elif msg == get_word('change phone number', update):
        user = get_user_by_update(update)
        text = get_word('your phone number', update).replace('<>', user.phone) + '\n\n' + get_word('send new phone number', update)
        i_contact = KeyboardButton(text=get_word('leave number', update), request_contact=True)
        i_back = KeyboardButton(text=get_word('back', update))
        update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup([[i_contact], [i_back]], resize_keyboard=True), parse_mode=telegram.ParseMode.HTML)
        return PHONE_SETTINGS
    elif msg == get_word('change name', update):
        user = get_user_by_update(update)
        text = get_word('your name', update) + user.name + '\n\n' + get_word('send new name', update)
        update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True), parse_mode=telegram.ParseMode.HTML)
        return NAME_SETTINGS



#  lang settings
@is_start
def lang_settings(update, context):
    update = update.callback_query
    bot = context.bot
    data = str(update.data)
    user = Bot_user.objects.get(user_id=update.message.chat.id)
    if data == 'set_lang_uz':
        user.lang = 'uz'
        user.save()
    elif data == 'set_lang_ru':
        user.lang = 'ru'
        user.save()
    elif data == 'back_settings':
        bot.delete_message(update.message.chat.id, update.message.message_id)
        make_button_settings(update, context)
        return ALL_SETTINGS
    current_lang = user.lang
    if current_lang == 'uz':
        uz_text = 'UZ \U0001F1FA\U0001F1FF   ✅'
        ru_text = 'RU \U0001F1F7\U0001F1FA'
    else:
        uz_text = 'UZ \U0001F1FA\U0001F1FF'
        ru_text = 'RU \U0001F1F7\U0001F1FA    ✅'
    
    i_uz = InlineKeyboardButton(text=uz_text, callback_data='set_lang_uz')
    i_ru = InlineKeyboardButton(text=ru_text, callback_data='set_lang_ru')
    i_back = InlineKeyboardButton(get_word('back', update), callback_data='back_settings')
    update.edit_message_text(get_word('select lang', update), reply_markup = InlineKeyboardMarkup([[i_uz], [i_ru], [i_back]]))


#phone settings
@is_start
def phone_settings(update, context):
    if update.message.contact == None or not update.message.contact:
        msg = update.message.text
        if msg == get_word('back', update):
            make_button_settings(update, context)
            return ALL_SETTINGS
        phone_number = update.message.text
    else:
        phone_number = update.message.contact.phone_number
    
    # check that phone is available or no
    is_available = Bot_user.objects.filter(phone=phone_number)
    if is_available:
        update.message.reply_text(get_word('number is logged',update))
        return PHONE_SETTINGS
    obj = Bot_user.objects.get(user_id=update.message.chat.id)
    obj.phone = phone_number
    obj.save()
    update.message.reply_text(get_word('changed your phone number', update))
    make_button_settings(update, context)
    return ALL_SETTINGS

#name settings
@is_start
def name_settings(update, context):
    msg = update.message.text
    if msg == get_word('back', update):
        make_button_settings(update, context)
        return ALL_SETTINGS
    new_name = msg
    obj = get_user_by_update(update)
    obj.name = new_name
    obj.save()
    update.message.reply_text(get_word('changed your name', update))
    make_button_settings(update, context)
    return ALL_SETTINGS
