import json


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
'''Получаем список словарей'''

def filter_data(data):
    for value in data:
        print(value['state'])