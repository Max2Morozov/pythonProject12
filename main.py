from utils import get_data, filter_data, sort_data, format_data


def main(name):
    #Получение данных из файла
    data = get_data()

    #Фильтрация транзакций
    data = filter_data(data)

    #Сортировка транзакций
    data = sort_data(data)

    #Проверка дат и счета и стрелок
    data = format_data(data)

    for row in data:
        print(row)



#if __name__ == '__main__':
    #main()