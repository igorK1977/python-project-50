from gendiff.formatter import format_diff, format_value
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_text_file(filename):
    return get_test_data_path(filename).read_text()

def test_format_value():
    assert format_value(False) == 'false'
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'
    assert format_value('') == ''
    assert format_value(123) == 123

def test_format_diff():
    diff = [{'key': 'common', 'status': 'nonchanged', 'value': [
                {'key': 'follow', 'status': 'added', 'value': False}, 
                {'key': 'setting1', 'value': 'Value 1', 'status': 'nonchanged'}, 
                {'key': 'setting2', 'value': 200, 'status': 'deleted'}, 
                {'key': 'setting3', 'status': 'changed', 'value': True, 'new_value': None}, 
                {'key': 'setting4', 'status': 'added', 'value': 'blah blah'}, 
                {'key': 'setting5', 'status': 'added', 'value': [
                    {'key': 'key5', 'status': 'nonchanged', 'value': 'value5'}]}, 
                {'key': 'setting6', 'status': 'nonchanged', 'value': [
                    {'key': 'doge', 'status': 'nonchanged', 'value': [
                        {'key': 'wow', 'status': 'changed', 'value': '', 'new_value': 'so much'}]}, 
                    {'key': 'key', 'value': 'value', 'status': 'nonchanged'}, 
                    {'key': 'ops', 'status': 'added', 'value': 'vops'}]}]}, 
                {'key': 'group1', 'status': 'nonchanged', 'value': [
                    {'key': 'baz', 'status': 'changed', 'value': 'bas', 'new_value': 'bars'}, 
                    {'key': 'foo', 'value': 'bar', 'status': 'nonchanged'}, 
                    {'key': 'nest', 'status': 'changed', 'value': [
                        {'key': 'key', 'status': 'nonchanged', 'value': 'value'}], 'new_value': 'str'}]}, 
                {'key': 'group2', 'value': [
                    {'key': 'abc', 'status': 'nonchanged', 'value': 12345}, 
                    {'key': 'deep', 'status': 'nonchanged', 'value': [
                        {'key': 'id', 'status': 'nonchanged', 'value': 45}]}], 'status': 'deleted'}, 
                {'key': 'group3', 'status': 'added', 'value': [
                    {'key': 'deep', 'status': 'nonchanged', 'value': [
                        {'key': 'id', 'status': 'nonchanged', 'value': [
                            {'key': 'number', 'status': 'nonchanged', 'value': 45}]}]}, 
                    {'key': 'fee', 'status': 'nonchanged', 'value': 100500}]}]
    
    expected = read_text_file('generate_diff_expected.txt')
    assert format_diff(diff, 'stylish') == expected