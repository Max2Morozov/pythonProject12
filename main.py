from utils import get_data, filter_data


def main(name):
    print('Получение данных из файла... ', end='')
    data = get_data()
    print("OK")

    data = filter_data(data)



if __name__ == '__main__':
    main()