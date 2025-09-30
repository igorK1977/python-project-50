def format_diff_stylish(diff):
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
                        diff_list.append(prefix + f'  {SYMB[value['status']]} {key}: {format(value['value'], level)}')
                    case 'changed':
                        diff_list.append(prefix + f'  {SYMB['deleted']} {key}: {format(value['value'], level)}')
                        diff_list.append(prefix + f'  {SYMB['added']} {key}: {format(value['new_value'], level)}')
            diff_list.append(prefix + '}')
            return '\n'.join(diff_list)
        else:
            return format_stylish_value(diff)
        
    return format(diff)