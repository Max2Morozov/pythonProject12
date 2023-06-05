from utils import sort_data


def test_sort_data(test_data):
    #for z in test_data:
        #print(z['date'])
    sorted_data = sort_data(test_data)
    for a in sorted_data:
        print(a['date'])