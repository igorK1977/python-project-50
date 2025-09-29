from gendiff.comparator import create_diff, data_to_diff


def test_date_to_diff():
    data = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    expected = [
        {'key': 'host', 'status': 'nonchanged', 'value': 'hexlet.io'},
        {'key': 'timeout', 'status': 'nonchanged', 'value': 20},
        {'key': 'verbose', 'status': 'nonchanged', 'value': True}]
    assert data_to_diff(data) == expected

def test_create_diff(file_1_data, file_2_data, diff):
    assert create_diff(file_1_data, file_2_data) == diff