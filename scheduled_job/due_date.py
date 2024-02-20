from base.models import *
from datetime import date, datetime, timedelta
from django.db.models import CharField, Value, F, Q

def check_expires():
    today = datetime.today()
    today_text = '{}-{}-{}'.format(today.year, today.month, today.day)
    month_later = today + timedelta(days=30)
    month_later_text = '{}-{}-{}'.format(month_later.year, month_later.month, month_later.day)

    # filter expired and due date keys
    by_keys = Client.objects.filter(key_exp__range = ['2000-1-1', month_later_text])
    for client in by_keys:
        duedate, is_created = Duedate.objects.get_or_create(
            client = client,
            type = 'key'
        )
        duedate.due_date = client.key_exp
        duedate.is_called = False
        duedate.save()

    # filter expired and due date guvohnoma
    by_guvohnoma = Client.objects.filter(guvohnoma_exp__range = ['2000-1-1', month_later_text])
    for client in by_guvohnoma:
        duedate, is_created = Duedate.objects.get_or_create(
            client = client,
            type = 'guvohnoma'
        )
        duedate.due_date = client.guvohnoma_exp
        duedate.is_called = False
        duedate.save()

    # filter expired and due date tanirovka
    by_tanirovka = Client.objects.filter(type='tanirovka', expiry_date__range = ['2000-1-1', month_later_text])
    for client in by_tanirovka:
        duedate, is_created = Duedate.objects.get_or_create(
            client = client,
            type = 'tanirovka'
        )
        duedate.due_date = client.expiry_date
        duedate.is_called = False
        duedate.save()
    
    # filter expired and due date ishonchnoma
    by_ishonchnoma = Client.objects.filter(type='ishonchnoma', expiry_date__range = ['2000-1-1', month_later_text])
    for client in by_ishonchnoma:
        duedate, is_created = Duedate.objects.get_or_create(
            client = client,
            type = 'ishonchnoma'
        )
        duedate.due_date = client.expiry_date
        duedate.is_called = False
        duedate.save()
    

    # filter expired and due date taxi
    by_taxi = Client.objects.filter(type='taxi', expiry_date__range = ['2000-1-1', month_later_text])
    for client in by_taxi:
        duedate, is_created = Duedate.objects.get_or_create(
            client = client,
            type = 'taxi'
        )
        duedate.due_date = client.expiry_date
        duedate.is_called = False
        duedate.save()
    

    


    # delete updated due dates
    Duedate.objects.filter(client__key_exp__range = [month_later_text, '3000-1-1'], type='key').delete()
    Duedate.objects.filter(client__guvohnoma_exp__range = [month_later_text, '3000-1-1'], type='guvohnoma').delete()
    Duedate.objects.filter(
        client__expiry_date__range = [month_later_text, '3000-1-1'], 
        type__in = ['tanirovka', 'ishonchnoma', 'taxi']
        ).delete()
        
