from base.models import Bot_user, Client, SMStext
from data.config import BOT_TOKEN, ENVIRONMENT
import telegram
from datetime import date
from django.db.models.query import Q
import requests

def alert_clients():
    # YATT guvohnoma
    for client in Client.objects.filter(Q(type='ytt') | Q(type='tanirovka') | Q(type='yuridik')):
        # identidy due date
        if client.guvohnoma_exp:
            due_date = client.guvohnoma_exp
            #check date
            if is_upcoming_due_date(due_date):
                if is_upcoming_due_date(due_date) == 10:
                    send_sms(client, is_upcoming_due_date(due_date))
                send_tg_message(client, is_upcoming_due_date(due_date))
        if client.key_exp:
            due_date = client.key_exp
        elif client.expiry_date:
            due_date = client.expiry_date
        else:
            continue
        
        #check date
        if is_upcoming_due_date(due_date):
            if is_upcoming_due_date(due_date) == 10:
                send_sms(client, is_upcoming_due_date(due_date))
            send_tg_message(client, is_upcoming_due_date(due_date))
                


def is_upcoming_due_date(due_date):
    today = date.today()
    difference = due_date - today
    if difference.days <= 10 and difference.days >= 0:
        return difference.days
    else:
        return False


def send_sms(client, remaining_days):
    rephone = client.phone1.replace(" ", "")
    rephone = rephone.replace("-","")
    rephone = rephone.replace(".","")
    rephone = rephone.replace(")","")
    rephone = rephone.replace("(","")
    if len(rephone) == 13:
        rephone = rephone
    elif len(rephone) == 9:
        rephone = '+998' + str(rephone)
    elif len(rephone) == 12 and rephone[0] == '9':
        rephone = '+' + str(rephone)
    elif len(rephone) == 0 or len(rephone) == 1:
        rephone = False
    else:
        rephone = False
    if rephone:
        numberid = rephone

    if client.is_certificate_expired == 'in_ten_days':
        sms_id = 7 # guvohnoma
    elif client.is_key_expired == 'in_ten_days':
        sms_id = 8 # kalit
    elif client.is_t_expired == 'in_ten_days':
        sms_id = 9 # tonirovla
    try:
        text = SMStext.objects.get(pk=sms_id).text
    except:
        return 
    
    text = text.replace('**kun', str(remaining_days))
    text = text.replace('**nom', client.name)
    url = 'http://91.204.239.44/broker-api/send'
    headers = {'Content-type': 'application/json',  # Определение типа данных
            'Accept': 'text/plain',
            'Authorization': 'Basic eHhpYXNyOmJwOWJFTVA3ODI='}
    data = {
    "messages":
    [
    {
    "recipient":numberid,
    "message-id":"prime000019953",
        "sms":{
        "originator": "21ASR",
        "content": {
        "text": text
        }
        }
            }
        ]
    } 

    if ENVIRONMENT != 'local':
        requests.post(url, json=data, headers=headers)



def send_tg_message(client, remaining_days):
    if client.is_certificate_expired == 'in_ten_days':
        sms_id = 7 # guvohnoma
    elif client.is_key_expired == 'in_ten_days':
        sms_id = 8 # kalit
    elif client.is_t_expired == 'in_ten_days':
        sms_id = 9 # tonirovla

    try:
        text = SMStext.objects.get(pk=sms_id).text
    except:
        return 
    text = text.replace('**kun', str(remaining_days))

    bot = telegram.Bot(token = BOT_TOKEN)
    try:
        user_id = client.bot_user.user_id
        bot.sendMessage(chat_id=user_id, text=text)
    except:
        return