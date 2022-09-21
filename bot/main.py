from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import InputMediaVideo, InputMediaPhoto
from telegram.ext import ConversationHandler

from base.models import *
from bot.conversationList import SELECT_LANG
from utils.bot import *
from control.settings import BASE_DIR
from data.config import ADMINS
from bot.uz_ru import lang_dict

def start(update, context):
    bot = context.bot
    if str(update.message.chat.id) in ADMINS:
        update.message.reply_text('Assalom alaykum!\nSiz ushbu bot adminisiz')
    else:
        # notify admin that new user registred
        text = "<b>Yangi foydalanuvchi</b>\n\nNom: {}\nUsername: {}".format(
            update.message.chat.first_name,
            update.message.chat.username or '',
        )
        message = bot.send_message(
            chat_id=int(ADMINS[0]),  
            text=text, 
            parse_mode = telegram.ParseMode.HTML
        )
        msg.objects.create(
            user_id=update.message.chat.id, 
            forward_msg_id=message.message_id, 
            msg_id=update.message.message_id
        )

        text = lang_dict['hello text'][0]
        photo = open('files/main.jpg', 'rb')
        Bot_user.objects.get_or_create(user_id=update.message.chat.id)
        obj = Bot_user.objects.get(user_id=update.message.chat.id)
        obj.username=update.message.chat.username
        obj.firstname = update.message.chat.first_name
        obj.save()
        update.message.reply_photo(photo, caption=text, parse_mode=telegram.ParseMode.HTML)

def message(update, context):
    bot = context.bot
    if str(update.message.chat.id) in ADMINS:
        if update.message.reply_to_message:
            if update.message.reply_to_message.from_user.id == update.message.chat.id:
                return
            else:
                try:
                    msg_id = update.message.reply_to_message.message_id
                    msg_obj = msg.objects.get(forward_msg_id=msg_id)
                    user_id = msg_obj.user_id
                    message = bot.send_message(
                        chat_id=user_id, 
                        text=update.message.text, 
                        reply_to_message_id=msg_obj.msg_id
                    )
                    msg.objects.create(
                        user_id=update.message.chat.id, 
                        forward_msg_id=message.message_id, 
                        msg_id=update.message.message_id
                    )
                except Exception as e:
                    print(e)
        else:
            return
    else:
        obj = Bot_user.objects.get(user_id=update.message.chat.id)
        obj.username=update.message.chat.username
        obj.firstname = update.message.chat.first_name
        obj.save()
        if update.message.reply_to_message:
            if update.message.reply_to_message.from_user.id == update.message.chat.id:
                return
            else:
                msg_id = update.message.reply_to_message.message_id
                msg_obj = msg.objects.get(forward_msg_id=msg_id)
                user_id = msg_obj.user_id  

                message = bot.send_message(
                    chat_id=user_id,  
                    text=update.message.text, 
                    reply_to_message_id=msg_obj.msg_id
                )
                msg.objects.create(
                    user_id=update.message.chat.id, 
                    forward_msg_id=message.message_id, 
                    msg_id=update.message.message_id
                )
        else:
            message = bot.forward_message(
                chat_id=int(ADMINS[0]), 
                from_chat_id=update.message.chat.id, 
                message_id=update.message.message_id,
            )
            msg.objects.create(
                user_id=update.message.chat.id, 
                forward_msg_id=message.message_id, 
                msg_id=update.message.message_id
            )

# def start(update, context):
    
#     if is_registered(update.message.chat.id):
#         main_menu(update, context)
#     else:
#         hello_text = '🤖 Xush kelibsiz!\n Bot tilini tanlang  🌎 \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\n 👋 Добро пожаловать \n \U0001F1FA\U0001F1FF Выберите язык бота \U0001F1F7\U0001F1FA'
#         update.message.reply_text(hello_text, reply_markup=ReplyKeyboardMarkup(keyboard=[['UZ 🇺🇿', 'RU 🇷🇺']], resize_keyboard=True))
#         return SELECT_LANG


# def settings(update, context):
#     make_button_settings(update, context)
#     return ALL_SETTINGS

# def cabinet(update, context):
#     if is_authorized(update):
#         make_my_cabinet(update, context)
#         return MY_CABINET
#     else:
#         update.message.reply_text(get_word('type login', update), reply_markup = 
#             ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True))
#         return GET_LOGIN

# def address(update, context):
#     bot = context.bot
#     bot.send_message(update.message.chat.id, get_word('all addresses', update), parse_mode = telegram.ParseMode.HTML)

#     bot.send_message(update.message.chat.id, get_word('1st office', update), parse_mode = telegram.ParseMode.HTML)
#     bot.send_location(update.message.chat.id, 39.4287332, 67.2386705)
    
#     bot.send_message(update.message.chat.id, get_word('2nd office', update), parse_mode = telegram.ParseMode.HTML)
#     bot.send_location(update.message.chat.id, 39.4178555, 67.2393289)
    
    
#     bot.send_message(update.message.chat.id, get_word('3rd office', update), parse_mode = telegram.ParseMode.HTML)
#     bot.send_location(update.message.chat.id, 39.4259444, 67.2368611)

# def our_services(update, context):
#     bot = context.bot
#     keyboard_words = ['accounting', 'car number', 'tonirovka', 'yagona darcha', 'auction', 'kochmas mulk', 'stamp', 'main menu']
#     keyboard = [[get_word(i, update)] for i in keyboard_words]
#     bot.send_message(update.message.chat.id, get_word('our all services', update), reply_markup = 
#         ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

#     # video = open(str(BASE_DIR) + '/static/videos/auksion.mp4', 'rb')
#     video = 'BAACAgIAAxkBAAIJrWKwf5s7fv8htJB4UoLXjgZ2EmT8AAJFGQACLDkYSBUAAXzop9QZOSgE'
#     try:
#         bot.send_video(chat_id = update.message.chat.id, video=video)
#     except:
#         a=0
#     return GET_SERVICE


# def contacts(update, context):
#     main_office = '<b>{}</b>: +998557012100'.format(get_word('main office', update))
#     car_number = '<b>{}</b>: +998992231118'.format(get_word('car number', update))
#     cadastre = '<b>{}</b>: +998992231115'.format(get_word('cadastre', update))
#     pc_service = '<b>{}</b>: +998901962266'.format(get_word('pc service', update))
#     msg = '{}\n\n{}\n\n{}\n\n{}'.format(main_office, car_number, cadastre, pc_service)
#     update.message.reply_text(msg, parse_mode=telegram.ParseMode.HTML)

# def send_video_id(update, context):
#     update.message.reply_text(update.message.video.file_id)