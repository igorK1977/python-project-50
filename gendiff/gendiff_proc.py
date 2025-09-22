import argparse
import json


def read_file(file_path):
    #print(f'Read file: {file_path}')
    data = json.load(open(file_path))
    return data


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    keys = sorted(list(set(list(data1.keys()) + list(data2.keys()))))
    diff = []
    for key in keys:
        if key in data1 and key not in data2:
            diff.append(f'- {key}: {data1[key]}')
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f'  {key}: {data1[key]}')
            else:
                diff.append(f'- {key}: {data1[key]}')
                diff.append(f'+ {key}: {data2[key]}')
        if key not in data1 and key in data2:
            diff.append(f'+ {key}: {data2[key]}')
    return '\n'.join(diff)


def request_proc():
    parser = argparse.ArgumentParser(
                    usage='gendiff [-h] first_file second_file',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))



