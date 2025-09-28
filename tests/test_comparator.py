from gendiff.comparator import create_diff, data_to_diff


def test_date_to_diff():
    data = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    expected = [
        {'key': 'host', 'status': 'nonchanged', 'value': 'hexlet.io'},
        {'key': 'timeout', 'status': 'nonchanged', 'value': 20},
        {'key': 'verbose', 'status': 'nonchanged', 'value': True}]

    assert data_to_diff(data) == expected

def test_create_diff():
    data1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    data2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    expected = [
        {'key': 'follow', 'value': False, 'status': 'deleted'},
        {'key': 'host', 'value': 'hexlet.io', 'status': 'nonchanged'},
        {'key': 'proxy', 'value': '123.234.53.22', 'status': 'deleted'},
        {'key': 'timeout', 'value': 50, 'status': 'changed', 'new_value': 20},
        {'key': 'verbose', 'status': 'added', 'value': True}]

    assert create_diff(data1, data2) == expected