from gendiff.gendiff_proc import generate_diff
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_generate_diff():
    FILE_NAME1 = 'file1.json'
    FILE_NAME2 = 'file2.json'
    file_path1 = get_test_data_path(FILE_NAME1)
    file_path2 = get_test_data_path(FILE_NAME2)
    expected = read_file('generate_diff_expected.txt')
    print(f'Test expected result = {expected}')
    assert generate_diff(file_path1, file_path2) == expected



