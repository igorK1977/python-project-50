import argparse
import json


def read_file(file_path):
    #print(f'Read file: {file_path}')
    data = json.load(open(file_path))
    return data


def request_proc():
    parser = argparse.ArgumentParser(
                    usage='gendiff [-h] first_file second_file',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    # read files
    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)

