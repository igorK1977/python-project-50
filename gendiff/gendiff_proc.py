import argparse
import json


def read_file(file_path):
    data = json.load(open(file_path))
    return data

def format(value):
    if isinstance(value, bool):
        json_value = json.dumps(value)
    else:
        json_value = value
    return json_value

def create_diff(data1, data2):
    keys = sorted(list(set(list(data1.keys()) + list(data2.keys()))))
    diff = []
    for key in keys:
        item = {'key': key}
        if key in data1 and key not in data2:
            item['value'] = data1[key]
            item['status'] = 'deleted'
        if key in data1 and key in data2:
            item['value'] = data1[key]
            if data1[key] == data2[key]:
                item['status'] = 'nonchanged'
            else:
                item['status'] = 'changed'
                item['new_value'] = data2[key]
        if key not in data1 and key in data2:
            item['status'] = 'added'
            item['value'] = data2[key]
        diff.append(item)
    return diff

def format_diff(diff):
    diff_list = []
    for item in diff:
        match item['status']:
            case 'nonchanged':
                diff_list.append(f'  {item['key']}: {format(item['value'])}')
            case 'deleted':
                diff_list.append(f'- {item['key']}: {format(item['value'])}')
            case 'added':
                diff_list.append(f'+ {item['key']}: {format(item['value'])}')
            case 'changed':
                diff_list.append(f'- {item['key']}: {format(item['value'])}')
                diff_list.append(f'+ {item['key']}: {format(item['new_value'])}')
    return '\n'.join(diff_list)

def generate_diff(file_path1, file_path2):
    data1, data2 = read_file(file_path1), read_file(file_path2)
    diff = create_diff(data1, data2)
    return format_diff(diff)

def request_proc():
    parser = argparse.ArgumentParser(
                    usage='gendiff [-h] first_file second_file',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))



