def format_plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        match value:
            case True:
                return 'true'
            case False:
                return 'false'
            case None:
                return 'null'
        return value


def format(diff, path=''):
    if isinstance(diff, dict):
        diff_list = []
        for key, value in diff.items():
            match value['status']:
                case 'deleted':
                    diff_list.append(f"Property '{path}{key}' was removed")
                case 'added':
                    str_value = format_plain_value(value['value'])
                    diff_list.append(
                        f"Property '{path}{key}' " + 
                        f"was added with value: {str_value}")
                case 'changed':
                    str_value = format_plain_value(value['value'])
                    str_new_value = format_plain_value(value['new_value'])
                    diff_list.append(
                        f"Property '{path}{key}' was updated. " + 
                        f"From {str_value} to {str_new_value}")
                case 'nonchanged':
                    result = format(value['value'], path + key + '.')
                    if result is not None:
                        diff_list.append(result)
        return '\n'.join(diff_list)


def format_plain(diff):
    return format(diff)