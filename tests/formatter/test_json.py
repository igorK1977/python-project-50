from gendiff.formatter.json import format_json


def test_format_json(diff, gendiff_json_expected):  
    assert format_json(diff) == gendiff_json_expected