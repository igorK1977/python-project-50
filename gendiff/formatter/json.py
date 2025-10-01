def format_json_value(value):
    if isinstance(value, str):
        return f'"{value}"'
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return value


def format(diff, level=0):
    PREFIX_DEFAULT = '  '
    if isinstance(diff, dict):
        diff_list = []
        prev_prefix = PREFIX_DEFAULT * level
        level += 1
        prefix = PREFIX_DEFAULT * level
        for key, value in diff.items():
            diff_list.append(prefix + f'"{key}": {format(value, level)}')
        return '{\n' + ',\n'.join(diff_list) + '\n' + prev_prefix + '}'
    else:
        return format_json_value(diff)


def format_json(diff):       
    return format(diff)