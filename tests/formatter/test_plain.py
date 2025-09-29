from gendiff.formatter.plain import format_diff_plain


def test_format_diff_plain(diff, gendiff_plain_expected):  
    assert format_diff_plain(diff) == gendiff_plain_expected
