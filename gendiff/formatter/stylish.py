def format_stylish_value(value):
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return value


def format(diff, level=-1):
    PREFIX_DEFAULT = '    '
    SYMB = {'nonchanged': ' ', 'deleted': '-', 'added': '+'}
    if isinstance(diff, dict):
        diff_list = ['{']
        level += 1
        prefix = PREFIX_DEFAULT * max(0, level)
        for key, value in diff.items():
            match value['status']:
                case 'nonchanged' | 'deleted' | 'added':
                    str_prefix = prefix + f'  {SYMB[value['status']]} '
                    str_val = f'{key}: {format(value['value'], level)}'
                    diff_list.append(str_prefix + str_val)
                case 'changed':
                    # add old value
                    str_prefix = prefix + f'  {SYMB['deleted']} '
                    str_val = f'{key}: {format(value['value'], level)}'
                    diff_list.append(str_prefix + str_val)
                    # add new value
                    str_prefix = prefix + f'  {SYMB['added']} '
                    str_val = f'{key}: {format(value['new_value'], level)}'
                    diff_list.append(str_prefix + str_val)
        diff_list.append(prefix + '}')
        return '\n'.join(diff_list)
    else:
        return format_stylish_value(diff)


def format_stylish(diff):
    return format(diff)