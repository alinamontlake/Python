import requests;
from decimal import *
from datetime import datetime
getcontext().prec = 4

def currency_rates(cur_name):
    
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(URL).text
    cur_name = cur_name.upper()

    if cur_name not in response:
        return None

    date = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, date)


    response = response[response.find(cur_name):]
    response = response[:response.find('</Value>')]
    new_response = response[response.find('<Value>') + 7:]

    return f"{Decimal(new_response.replace(',', '.'))},{datetime(day = day, month = month, year = year)}"

if __name__ == '__main__':
    print(*currency_rates('USD'))
    print(*currency_rates('EUR'))
