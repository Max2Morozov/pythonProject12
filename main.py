from utils import get_data, filter_data, sort_data, format_data

PATH_TO_OPERATIONS = 'operations.json'
def main():
    #Получение данных из файла
    data = get_data(PATH_TO_OPERATIONS)

    #Фильтрация транзакций
    data = filter_data(data)

    #Сортировка транзакций
    data = sort_data(data)

    #Проверка дат и счета и стрелок
    data = format_data(data)

    for row in data:
        print(row)

main()