from gendiff.gendiff_processing import read_file
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_text_file(filename):
    return get_test_data_path(filename).read_text()

def test_read_file_incorr_format():
    FILE_NAME = 'file1.txt'

    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) is None

def test_read_file():
    expected = {
        "common": {
            "setting1": "Value 1", 
            "setting2": 200, 
            "setting3": True, 
            "setting6": {
                "key": "value", 
                "doge": {"wow": ""}}}, 
            "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}}, 
            "group2": {"abc": 12345, "deep": {"id": 45}}}
    FILE_NAME = 'file1.json'
    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) == expected

    FILE_NAME = 'file1.yml'
    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) == expected

    FILE_NAME = 'file1.yaml'
    file_path = get_test_data_path(FILE_NAME)
    assert read_file(file_path) == expected
