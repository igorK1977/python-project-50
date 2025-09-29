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
        if isinstance(diff, list):
            diff_list = ['{']
            level += 1
            prefix = PREFIX_DEFAULT * max(0, level)
            for item in diff:
                match item['status']:
                    case 'nonchanged' | 'deleted' | 'added':
                        diff_list.append(prefix + f'  {SYMB[item['status']]} {item['key']}: {format(item['value'], level)}')
                    case 'changed':
                        diff_list.append(prefix + f'  {SYMB['deleted']} {item['key']}: {format(item['value'], level)}')
                        diff_list.append(prefix + f'  {SYMB['added']} {item['key']}: {format(item['new_value'], level)}')
            diff_list.append(prefix + '}')
            return '\n'.join(diff_list)
        else:
            return format_stylish_value(diff)
        
    return format(diff)