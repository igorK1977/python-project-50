from gendiff.formatter.stylish import format_stylish


def test_format_stylish(diff, gendiff_stylish_expected):  
    assert format_stylish(diff) == gendiff_stylish_expected

