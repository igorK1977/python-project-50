import argparse
from gendiff.file_parsing import read_file
from gendiff.comparator import create_diff
from gendiff.formatter import format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = read_file(file_path1), read_file(file_path2)
    if all([data1, data2]):
        diff = create_diff(data1, data2)
    else:
        return None
    return format_diff(diff, format_name)

def request_processing():
    parser = argparse.ArgumentParser(
                    usage='gendiff [-h] first_file second_file',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))



