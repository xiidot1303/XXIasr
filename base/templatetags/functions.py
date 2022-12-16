from django import template
from base.models import Client
from django.db.models import CharField, Value, F, Q
from datetime import date, timedelta
from itertools import chain
import os

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def filename(value):
    if value:
        return os.path.basename(value.file.name)
    return ''
@register.filter
def expired_dates(zero):
    today = date.today()
    today_text = '{}-{}-{}'.format(today.year, today.month, today.day)
    month_later = today + timedelta(days=30)
    month_later_text = '{}-{}-{}'.format(month_later.year, month_later.month, month_later.day)



    by_key = Client.objects.filter(Q(type='ytt') | Q(type='yuridik'), key_exp__range = [today_text, month_later_text]).values(
        exp_date=F('key_exp'), exp_type=Value('key', output_field=CharField())).values()
    
    by_guvohnoma = Client.objects.filter(type='ytt', guvohnoma_exp__range = [today_text, month_later_text]).values(
        exp_date=F('guvohnoma_exp'), exp_type=Value('guvohnoma', output_field=CharField())).values()
    
    by_expiry_date = Client.objects.filter(type='tanirovka', expiry_date__range = [today_text, month_later_text]).values(
        exp_date=F('expiry_date'), exp_type=Value('tonirovka', output_field=CharField())).values()
    
    all = list(chain(by_key, by_guvohnoma, by_expiry_date))
    all.sort(key=lambda x: x['exp_date'])
    return all

@register.filter
def define_msg(obj):
    exp_date = obj['exp_date']
    today = date.today()
    remaining_days = (exp_date - today).days
    texts_expired = {
        'key': ['Kalit muddati tugashiga {} kun qoldi', 'Kalit muddati tugagan'],
        'guvohnoma': ['Guvohnoma muddati tugashiga {} kun qoldi', 'Guvohnoma muddati tugagan'],
        'tonirovka': ['Tonirovka muddati tugashiga {} kun qoldi', 'Tonirovka muddati tugagan'],

    }
    if remaining_days > 0: # exp date is coming
        r_text = texts_expired[obj['exp_type']][0].format(remaining_days)
    else:
        r_text = texts_expired[obj['exp_type']][1]

    return r_text

@register.filter
def define_label(obj):
    exp_date = obj['exp_date']
    today = date.today()
    remaining_days = (exp_date - today).days
    if remaining_days > 20:
        label = 'bg-primary'
    
    elif remaining_days > 15:
        label = 'bg-info'
    
    elif remaining_days > 10:
        label = 'bg-light'
    
    elif remaining_days > 5:
        label = 'bg-warning'
    
    elif remaining_days > 0:
        label = 'bg-danger'
    
    else:
        label = 'bg-dark'
    return label
    
@register.filter
def filter_keys_by_type(keys, type):
    if type[0] == 'all':
        return keys
    return keys.filter(type=type[0])

@register.filter
def type_readable(type):
    TYPE_CHOICES = {
        'ytt': 'YaTT',
        'yuridik': 'Yuridik shaxs',
        'jismoniy': 'Jismoniy shaxs',
        'tanirovka':'Tanirovka',
        'auction':'Avtoraqam',
        'auction2':'Auksion',
        'teacher':"O'qituvchi",
        'governor': 'Hokim yordamchisi',
        'taxi': 'Taxi litsenziya',
        'ishonchnoma': 'Ishonchnoma',
    }
    return TYPE_CHOICES[type]