
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