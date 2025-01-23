from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import InputMediaVideo, InputMediaPhoto, MenuButtonCommands
from telegram.ext import ConversationHandler
from telegram import Bot
from base.models import *
from bot2.conversationList import *
from control.settings import BASE_DIR
from data.config import ADMINS
from base.models import MiniUpload


def start(update, context):
    text = f"Assalomu aleykum {update.message.chat.first_name}\n\nKontaktni ulashganingizdan so'ng biz sizga xizmatlar ro'yxatini taqdim etamiz!"    
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(
                text="📞 Kontaktni ulashish",
                request_contact=True
            )
        ]], resize_keyboard=True
    )
    update.message.reply_text(text, reply_markup=reply_markup)
    return GET_CONTACT


def get_contact(update: Update, context):
    phone = update.message.contact.phone_number
    context.user_data['phone'] = phone
    text = f"Sizning telefon raqamingiz: {phone}.\n" \
        "Xizmatni tanlaganingizdan so'ng operatorlarimiz sizga aloqaga chiqishadi.\n\n" \
            "Iltimos, xizmat turini yozing..."
    markup = ReplyKeyboardRemove()
    update.message.reply_text(text, reply_markup=markup)
    return GET_SERVICE


def get_service(update: Update, context):
    bot: Bot = context.bot
    service = update.message.text
    text = f"Murojaatingiz  uchun  rahmat  {update.message.chat.first_name}\n" \
        f"<b>{service}</b> xizmatini tanladingiz. Biz sizga tez orada aloqaga chiqamiz.\n\n" \
            "Qaytatdan ariza qoldirish uchun /start ustiga bosing."
    update.message.reply_html(text)
    phone = context.user_data['phone']
    # create mini upload
    receiver = Profile.objects.filter(user__username = "shoxsaidshohjaxon").first()
    mini = MiniUpload.objects.create(
        receiver=receiver, name=update.message.chat.first_name,
        phone=phone, service=service
        )
    print(mini)
    return ConversationHandler.END
