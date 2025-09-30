from gendiff.formatter.json import format_diff_json


def test_format_diff_json(diff, gendiff_json_expected):  
    assert format_diff_json(diff) == gendiff_json_expected