from gendiff.gendiff_proc import generate_diff
from pathlib import Path
import pytest
import os


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_text_file(filename):
    return get_test_data_path(filename).read_text()

@pytest.fixture
def file_path1():
    FILE_NAME = 'file1.json'
    file_path = get_test_data_path(FILE_NAME)  
    return file_path

@pytest.fixture
def file_path2():
    FILE_NAME = 'file2.json'
    file_path = get_test_data_path(FILE_NAME)  
    return file_path

@pytest.fixture
def gendiff_expected():
    return read_text_file('generate_diff_expected.txt')

def test_generate_diff(file_path1, file_path2, gendiff_expected):
    assert generate_diff(file_path1, file_path2) == gendiff_expected

def test_request_gendiff(capfd, file_path1, file_path2, gendiff_expected):
    command = f'uv run gendiff {file_path1} {file_path2}'
    os.system(command)
    captured = capfd.readouterr()
    expected = gendiff_expected + '\n'
    assert captured.out == expected
