from base.models import *
from data.config import BOT_TOKEN
import telegram

from base.utils.get_object import *


def bot_send_message(client, text):

    user_id = get_bot_user_id_by_client(client)

    try:
        bot = telegram.Bot(token = BOT_TOKEN)
        bot.sendMessage(chat_id=user_id, text=text)
    except:
        ok = True
    