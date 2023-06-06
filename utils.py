import json
import os
from datetime import datetime

def get_data(path):
    '''Получаем список словарей'''
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filter_data(data):
    '''Проверяем значение EXECUTED и если в x нет значение, его отбрасываем.'''
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

        #def sorted_lambda_key(x):
        #'''Замена лямбды функции #data = sorted(data, key=lambda x: x['data'], reverse=True)
        # на key=sorted_lambda_key, reverse=True'''
        #return x['date']

def sort_data(data):
    '''Сортировка транзакций через лямда функцию, списком дату '''
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]

def format_data(data):
    '''Добавляем сортировку даты и необходимые сведения'''
    formatted_data =[]
    for row in data:
        #"2019-07-13T18:51:29.313309"
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        # сжатие данных в необходимый нам формат данных
        description = row['description']
        if "from" in row: #проверка транзакций, куда ведет стрелка
            from_arrow = "->"
            sender = row['from'].split() #значение VISA или Classic
            sender_bill = sender.pop(-1) #забираем последнее значение (счет), знаем что оно верное
            sender_info = " ".join(sender) #знаем, что тут информация о счете
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}" #данные о карте



        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""
        send_bill = row['to'].split()  # сведения о счете
        bill = send_bill.pop(-1)
        bill_info = ' '.join(send_bill)
        bill = f'**{bill[-4:]}'
        operation_sum = row['operationAmount']['amount']
        operation_currency = row['operationAmount']['currency']['name']

        formatted_data.append(f"""{date} {description}
{sender_info} {sender_bill} {from_arrow} {bill_info} {bill}
{operation_sum} {operation_currency}""")
    return formatted_data

