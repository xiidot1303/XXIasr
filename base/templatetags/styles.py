from django import template

register = template.Library()

@register.filter
def car_number(number):
    n = number
    try:
        result = '{} {} {} {}'.format(n[:2], n[2], n[3:6], n[6:])
    except:
        result = number
    return result