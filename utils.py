import json


def get_data():
    '''Получаем список словарей'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    '''Проверяем значение EXECUTED и если в x нет значение, его отбрасываем.'''
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def sort_data(data):
    '''Сортировка транзакций через лямда функцию, EXECUTED и если в x нет значение, его отбрасываем.'''
    data = sorted(data, key=lambda x: x['data'], reverse=True)
    return data[:5]