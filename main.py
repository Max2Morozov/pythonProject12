from utils import get_data, filter_data, sort_data, format_data


def main(name):
    #print('Получение данных из файла... ', end='')
    data = get_data()
    #print("OK")

    #print('Фильтрация транзакций... ', end='')
    data = filter_data(data)
    #print("OK")

    #print('Сортировка транзакций... ', end='')
    data = sort_data(data)
    #print("OK")

    #print('Проверка дат и счета и стрелок... ', end='')
    data = format_data(data)
    #print("OK")

    for row in data:
        print(row)



if __name__ == '__main__':
    main()