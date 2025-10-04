from gendiff.formatters.plain import format_plain


def test_format_plain(diff, gendiff_plain_expected):  
    assert format_plain(diff) == gendiff_plain_expected
