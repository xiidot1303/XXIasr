from base.models import *
from data.config import BOT_TOKEN
import telegram

from base.utils.get_object import *
import requests
from data.config import ENVIRONMENT

def bot_send_message(client, text):

    user_id = get_bot_user_id_by_client(client)

    try:
        bot = telegram.Bot(token = BOT_TOKEN)
        bot.sendMessage(chat_id=user_id, text=text)
    except:
        ok = True
    
def send_sms(client, text):

    # edit number
    numberid = 969769789
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

    # send sms
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
