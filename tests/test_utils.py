from utils import sort_data


def test_sort_data(test_data):
    #for z in test_data:
        #print(z['date'])
    sorted_data = sort_data(test_data)
    #for a in sorted_data:
        #print(a['date'])
    assert [x['date'] for x in sorted_data] == \
           ['2019-08-26T10:50:58.294041',
            '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']