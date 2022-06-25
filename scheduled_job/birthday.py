from base.models import Bot_user, Client, SMStext
from data.config import BOT_TOKEN, ENVIRONMENT
import telegram
from datetime import date
from django.db.models.query import Q
import requests
from base.utils import message



def day_and_month():
    today = date.today()
    day_and_month_ = ''
    if len(str(today.day)) == 1:
        day_and_month_ += '0' + str(today.day)
    else:
        day_and_month_ += str(today.day)
    if len(str(today.month)) == 1:
        day_and_month_ += '0' + str(today.month)
    else:
        day_and_month_ += str(today.month)
    return day_and_month_

def send_congragulation():
    for client in Client.objects.filter(jshshir__icontains = day_and_month()):
        if is_birthday(client.jshshir):
            try:
                text = SMStext.objects.get(pk=10).text
                text = text.replace('**nom', client.name)
                message.bot_send_message(client, text)
                message.send_sms(client, text)
            except:
                a=0
    

    

def is_birthday(jshshir):
    if jshshir:
        if jshshir[1:5] == day_and_month():
            return True
    return False