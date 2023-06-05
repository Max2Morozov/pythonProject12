import os
from utils import sort_data, filter_data, get_data, format_data


def test_sort_data(test_data):
    '''test_data это список из conftest, для теста. Мы передаем этот список в функцию
    и получаем сортированный список значений. И date находиться в определенном порядке, список 2019-08-26 и тд.
    '''
    #for z in test_data:
        #print(z['date'])
    sorted_data = sort_data(test_data)
    #for a in sorted_data:
        #print(a['date'])
    assert [x['date'] for x in sorted_data] == \
           ['2019-08-26T10:50:58.294041',
            '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']
    def test_load_data():
        assert get_data(os.path('operation_file.json')) == []
        assert get_data(os.path('test_operations.json')) == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },
        ]

    def test_sorted_by_state(test_data):
        sort_by_state = filter_data(test_data)
        assert [x['state'] for x in sort_by_state if x['state'] == 'EXECUTED'] == ['EXECUTED', 'EXECUTED']

    def test_format_data():
        assert format_data([{
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        ]) == ['23.03.2018 Открытие вклада\nНовый счет  : Счет **2431\n48223.05 руб.\n']
        assert format_data([{
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        ]) == ['23.03.2019 Перевод со счета на счет\nСчет 4481 22** **** 4719 -> Счет **1160\n43318.34 руб.\n']
