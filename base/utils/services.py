from base.models import Client, Key


def get_uzb_month(month):
    return uzb_months[month-1]

def number_format(number):
    try:
        number = int(number)
        text = '{:,}'.format(number).replace(',', ' ')
    except:
        text = number
    return text

uzb_months = [
    'Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 
    'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr'
    ]

def create_key(client_pk, profile):
    client = Client.objects.get(pk=client_pk)
    if client.key:
        if not Key.objects.filter(key=client.key, client__pk=client.pk, key_exp=client.key_exp):
            Key.objects.create(
                client=client, type=client.type, added_by=profile,
                name=client.name, key=client.key, key_exp=client.key_exp, jshshir=client.jshshir
            )


def handle_uploaded_file(f):
    with open(f'static/keys/{f}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f'static/keys/{f}'