from gendiff.formatter.stylish import format_diff_stylish


def test_format_diff(diff, gendiff_stylish_expected):  
    assert format_diff_stylish(diff) == gendiff_stylish_expected

