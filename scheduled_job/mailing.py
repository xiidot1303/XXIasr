from base.models import Bot_user, Client, telegramPost
from data.config import BOT_TOKEN, ENVIRONMENT
import telegram
from datetime import date
from django.db.models.query import Q
import requests
from data.config import BOT_TOKEN

def send_message():
    for post in telegramPost.objects.all():
        bot = telegram.Bot(token = BOT_TOKEN)
        if post.client_type != 'all':
            subs = Client.objects.filter(type=post.client_type).exclude(bot_user=None)
        else:
            subs = Bot_user.objects.exclude(phone = None)
        for sub in subs:
            if post.client_type == 'all':
                user_id = sub.user_id
            else:
                user_id = sub.bot_user.user_id
            try:
                if post.post_type == 'text':
                    bot.sendMessage(chat_id=user_id, text = post.text, parse_mode=telegram.ParseMode.HTML)
                elif post.post_type == 'photo':
                    bot.sendPhoto(chat_id=user_id, photo=post.file, caption=post.text)
                elif post.post_type == 'video':
                    bot.sendVideo(chat_id=user_id, video=post.file, caption=post.text)
                elif post.post_type == 'audio':
                    bot.sendAudio(chat_id=user_id, audio=post.file, caption=post.text)
                elif post.post_type == 'document':
                    bot.sendDocument(chat_id=user_id, document=post.file, caption=post.text)
            except:
                a = 0
        post.delete()

