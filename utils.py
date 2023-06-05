import json
from datetime import datetime

def get_data():
    '''Получаем список словарей'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    '''Проверяем значение EXECUTED и если в x нет значение, его отбрасываем.'''
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def sorted_lambda_key(x):
    '''Замена лямбды функции #data = sorted(data, key=lambda x: x['data'], reverse=True)
     на key=sorted_lambda_key, reverse=True'''
    return x['date']

def sort_data(data):
    '''Сортировка транзакций через лямда функцию, списком дату '''
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]

def format_data(data):
    '''Добавляем сортировку даты и необходимые сведения'''
    formatted_data =[]
    for row in data:
        #"2019-07-13T18:51:29.313309"
        date = datetime.strftime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        # сжатие данных в необходимый нам формат данных
        description = row['description']
        if "from" in row: #проверка транзакций, куда ведет стрелка
            from_arrow = "->"
            sender = row['from'].split() #значение VISA или Classic
            sender_bill = sender.pop(-1) #забираем последнее значение (счет), знаем что оно верное
            sender_info = " ".join(sender) #знаем, что тут информация о счете
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""

        formatted_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow}\
        """)
    return formatted_data

