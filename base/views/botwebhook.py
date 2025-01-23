from telegram import Update
from django.views.decorators.csrf import csrf_exempt
from data.config import ENVIRONMENT
from django.http.response import HttpResponse
from bot2.update import dp, updater
import json


@csrf_exempt
def bot_webhook(request):

    if ENVIRONMENT == 'local':
        updater.start_polling()
    else:
        update = Update.de_json(json.loads(request.body.decode('utf-8')), dp.bot)
        dp.process_update(update)
    return HttpResponse('Bot started!')