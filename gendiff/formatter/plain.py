def format_diff_plain(diff):
    def format_plain_value(value):
        if isinstance(value, dict):
            return '[complex value]'
        else:
            if isinstance(value, str):
                return f"'{value}'"
            match value:
                case True:
                    return 'true'
                case False:
                    return 'false'
                case None:
                    return 'null'
                case _:
                    return value
                
    def format(diff, path=''):
        if isinstance(diff, dict):
            diff_list = []
            for key, value in diff.items():
                match value['status']:
                    case 'deleted':
                        diff_list.append(f"Property '{path}{key}' was removed")
                    case 'added':
                        diff_list.append(f"Property '{path}{key}' was added with value: {format_plain_value(value['value'])}")
                    case 'changed':
                        diff_list.append(f"Property '{path}{key}' was updated. From {format_plain_value(value['value'])} to {format_plain_value(value['new_value'])}")
                    case 'nonchanged':
                        result = format(value['value'], path + key + '.')
                        if result is not None:
                            diff_list.append(result)
            return '\n'.join(diff_list)
        
    return format(diff)