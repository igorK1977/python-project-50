from gendiff.gendiff_processing import read_file


def test_read_file_incorr_format():
    assert read_file('file1.txt') is None


def test_read_file(
        json_file_path1, yml_file_path1, yaml_file_path1, file_1_data):
    assert read_file(json_file_path1) == file_1_data
    assert read_file(yml_file_path1) == file_1_data
    assert read_file(yaml_file_path1) == file_1_data
