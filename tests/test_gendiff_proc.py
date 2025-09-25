from gendiff.gendiff_proc import generate_diff, create_diff, format_diff
from pathlib import Path
import os


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_text_file(filename):
    return get_test_data_path(filename).read_text()

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

def test_format_diff():
    diff = [
        {'key': 'follow', 'value': False, 'status': 'deleted'},
        {'key': 'host', 'value': 'hexlet.io', 'status': 'nonchanged'},
        {'key': 'proxy', 'value': '123.234.53.22', 'status': 'deleted'},
        {'key': 'timeout', 'value': 50, 'status': 'changed', 'new_value': 20},
        {'key': 'verbose', 'status': 'added', 'value': True}]
    expected = read_text_file('generate_diff_expected.txt')
    assert format_diff(diff) == expected

def test_generate_diff():
    FILE_NAME1 = 'file1.json'
    FILE_NAME2 = 'file2.json'
    file_path1 = get_test_data_path(FILE_NAME1)
    file_path2 = get_test_data_path(FILE_NAME2)
    expected = read_text_file('generate_diff_expected.txt')
    assert generate_diff(file_path1, file_path2) == expected

def test_request_gendiff(capfd):
    os.system('uv run gendiff /home/igor/files/file1.yml /home/igor/files/file2.yml')
    captured = capfd.readouterr()
    print(captured.out)
    expected = '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n'
    assert captured.out == expected
