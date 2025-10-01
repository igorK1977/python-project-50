import os

from gendiff.gendiff_processing import generate_diff


def test_generate_diff(
        json_file_path1, json_file_path2, gendiff_stylish_expected, 
        gendiff_plain_expected, gendiff_json_expected):
    assert generate_diff(
        json_file_path1, json_file_path2) == gendiff_stylish_expected
    assert generate_diff(
        json_file_path1, json_file_path2, 'plain') == gendiff_plain_expected
    assert generate_diff(
        json_file_path1, json_file_path2, 'json') == gendiff_json_expected


def test_request_gendiff(
        capfd, json_file_path1, json_file_path2, gendiff_stylish_expected, 
        gendiff_plain_expected, gendiff_json_expected):
    expected = gendiff_stylish_expected + '\n'

    os.system(f'uv run gendiff {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected

    os.system(
        f'uv run gendiff --format stylish {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected

    os.system(f'gendiff {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected

    os.system(
        f'gendiff --format stylish {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected

    expected = gendiff_plain_expected + '\n'

    os.system(
        f'uv run gendiff --format plain {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected

    os.system(f'gendiff --format plain {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected

    expected = gendiff_json_expected + '\n'

    os.system(
        f'uv run gendiff --format json {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected

    os.system(f'gendiff --format json {json_file_path1} {json_file_path2}')
    captured = capfd.readouterr()
    assert captured.out == expected