def format_diff_json(diff):
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

    def format(diff, level=-1):
        PREFIX_DEFAULT = '  '
        if isinstance(diff, list):
            diff_list = []
            level += 1
            prefix = PREFIX_DEFAULT * level
            for item in diff:
                if 'key' not in item:
                    diff_list.append(prefix + f'"status": {format(item['status'], level)}')
                    diff_list.append(prefix + f'"value": {format(item['value'], level)}')
                    if item['status'] == 'changed':
                        diff_list.append(prefix + f'"new_value": {format(item['new_value'], level)}')
                else:
                    match item['status']:
                        case 'nonchanged':
                            diff_list.append(prefix + f'"{item['key']}": {format([{'status': item['status'], 'value': item['value']}], level)}')
                        case 'deleted':
                            diff_list.append(prefix + f'"{item['key']}": {format([{'status': item['status'], 'value': item['value']}], level)}')
                        case 'added':
                            diff_list.append(prefix + f'"{item['key']}": {format([{'status': item['status'], 'value': item['value']}], level)}')                        
                        case 'changed':
                            diff_list.append(prefix + f'"{item['key']}": {format([{'status': item['status'], 'value': item['value'], 'new_value': item['new_value']}], level)}') 
            return '{\n' + ',\n'.join(diff_list) + '\n' + prefix + '}'
        else:
            return format_json_value(diff)
        
    return format(diff)