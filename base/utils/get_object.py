from base.models import *


def get_bot_user_id_by_client(client):
    if client.bot_user:
        return client.bot_user.user_id
    else:
        return None