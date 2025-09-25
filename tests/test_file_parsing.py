from gendiff.gendiff_proc import read_file
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_text_file(filename):
    return get_test_data_path(filename).read_text()

def test_read_file_incorr_format():
    FILE_NAME = 'file1.txt'

    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) is None

def test_read_file_json():
    FILE_NAME = 'file1.json'
    expected = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}

    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) == expected

def test_read_file_yml():
    FILE_NAME = 'file1.yml'
    expected = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}

    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) == expected

def test_read_file_yaml():
    FILE_NAME = 'file1.yaml'
    expected = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}

    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) == expected