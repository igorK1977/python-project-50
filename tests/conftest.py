from pathlib import Path

import pytest


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_text_file(filename):
    return get_test_data_path(filename).read_text()


@pytest.fixture
def json_file_path1():
    FILE_NAME = 'file1.json'
    return get_test_data_path(FILE_NAME) 


@pytest.fixture
def yml_file_path1():
    FILE_NAME = 'file1.yml'
    return get_test_data_path(FILE_NAME) 


@pytest.fixture
def yaml_file_path1():
    FILE_NAME = 'file1.yaml'
    return get_test_data_path(FILE_NAME) 


@pytest.fixture
def json_file_path2():
    FILE_NAME = 'file2.json'
    return get_test_data_path(FILE_NAME)


@pytest.fixture
def gendiff_plain_expected():
    return read_text_file('gendiff_plain_expected.txt')


@pytest.fixture
def gendiff_stylish_expected():
    return read_text_file('gendiff_stylish_expected.txt')


@pytest.fixture
def gendiff_json_expected():
    return read_text_file('gendiff_json_expected.txt')


@pytest.fixture
def file_1_data():
    return {
        "common": {
            "setting1": "Value 1", 
            "setting2": 200, 
            "setting3": True, 
            "setting6": {
                "key": "value", 
                "doge": {"wow": ""}}}, 
            "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}}, 
            "group2": {"abc": 12345, "deep": {"id": 45}}}


@pytest.fixture
def file_2_data():
    return {'common': {
        'follow': False, 
        'setting1': 'Value 1', 
        'setting3': None, 
        'setting4': 'blah blah', 
        'setting5': {'key5': 'value5'}, 
        'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 
        'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 
        'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}


@pytest.fixture
def diff():
    return {'common': {'status': 'nonchanged', 'value': 
                       {'follow': {'status': 'added', 'value': False}, 
                        'setting1': {'value': 'Value 1', 'status': 'nonchanged'}, 
                        'setting2': {'value': 200, 'status': 'deleted'}, 
                        'setting3': {'status': 'changed', 'value': True, 'new_value': None}, 
                        'setting4': {'status': 'added', 'value': 'blah blah'}, 
                        'setting5': {'status': 'added', 'value': 
                                     {'key5': {'status': 'nonchanged', 'value': 'value5'}}}, 
                        'setting6': {'status': 'nonchanged', 'value': 
                                     {'doge': {'status': 'nonchanged', 'value': 
                                               {'wow': {'status': 'changed', 'value': '', 'new_value': 'so much'}}}, 
                                               'key': {'value': 'value', 'status': 'nonchanged'}, 
                                               'ops': {'status': 'added', 'value': 'vops'}}}}}, 
            'group1': {'status': 'nonchanged', 'value': 
                       {'baz': {'status': 'changed', 'value': 'bas', 'new_value': 'bars'}, 
                        'foo': {'value': 'bar', 'status': 'nonchanged'}, 
                        'nest': {'status': 'changed', 'value': 
                                 {'key': {'status': 'nonchanged', 'value': 'value'}}, 'new_value': 'str'}}}, 
            'group2': {'value': {
                        'abc': {'status': 'nonchanged', 'value': 12345}, 
                        'deep': {'status': 'nonchanged', 'value': 
                                 {'id': {'status': 'nonchanged', 'value': 45}}}}, 
                                 'status': 'deleted'}, 
            'group3': {'status': 'added', 'value': 
                       {'deep': {'status': 'nonchanged', 'value': 
                                 {'id': {'status': 'nonchanged', 'value': 
                                         {'number': {'status': 'nonchanged', 'value': 45}}}}}, 
                        'fee': {'status': 'nonchanged', 'value': 100500}}}}
