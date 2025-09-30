import argparse
from gendiff.file_parsing import read_file
from gendiff.comparator import create_diff
from gendiff.formatter.stylish import format_diff_stylish
from gendiff.formatter.plain import format_diff_plain
from gendiff.formatter.json import format_diff_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = read_file(file_path1), read_file(file_path2)
    if all([data1, data2]):
        diff = create_diff(data1, data2)
    else:
        return None
    match format_name:
        case 'stylish': 
            return format_diff_stylish(diff)
        case 'plain': 
            return format_diff_plain(diff)
        case 'json':
            return format_diff_json(diff)
        case _: 
            return None

def request_processing():
    parser = argparse.ArgumentParser(
                    usage='gendiff [-h] first_file second_file',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    match args.format:
        case None : 
            print(generate_diff(args.first_file, args.second_file))
        case _: 
            print(generate_diff(args.first_file, args.second_file, args.format))

        



