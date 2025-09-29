def format_diff_plain(diff):
    def format_plain_value(value):
        if isinstance(value, list):
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
        if isinstance(diff, list):
            diff_list = []
            for item in diff:
                match item['status']:
                    case 'deleted':
                        diff_list.append(f"Property '{path + item['key']}' was removed")
                    case 'added':
                        diff_list.append(f"Property '{path + item['key']}' was added with value: {format_plain_value(item['value'])}")
                    case 'changed':
                        diff_list.append(f"Property '{path + item['key']}' was updated. From {format_plain_value(item['value'])} to {format_plain_value(item['new_value'])}")
                    case 'nonchanged':
                        result = format(item['value'], path + item['key'] + '.')
                        if result is not None:
                            diff_list.append(result)
            return '\n'.join(diff_list)
        
    return format(diff)