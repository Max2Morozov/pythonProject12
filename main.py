from utils import get_data


def main(name):
    print('Получение данных из файла')
    data = get_data()
    print(data)


if __name__ == '__main__':
    main()