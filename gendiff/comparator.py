def data_to_diff(data):
    if isinstance(data, dict):
        result = {}
        keys = sorted(list(set(list(data.keys()))))
        for key in keys:
            item = {'status': 'nonchanged', 'value': data_to_diff(data[key])}
            result[key] = item
        return result
    else:
        return data

def create_diff(data1, data2):
    keys = sorted(list(set(list(data1.keys()) + list(data2.keys()))))
    diff = {}
    for key in keys:
        item = {}
        if key in data1 and key not in data2:
            item['value'] = data_to_diff(data1[key])
            item['status'] = 'deleted'
        if key not in data1 and key in data2:
            item['status'] = 'added'
            item['value'] = data_to_diff(data2[key])
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                item['value'] = data_to_diff(data1[key])
                item['status'] = 'nonchanged'
            else:
                if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                    item['status'] = 'nonchanged'
                    item['value'] = create_diff(data1[key], data2[key])
                else:
                    item['status'] = 'changed'
                    item['value'] = data_to_diff(data1[key])
                    item['new_value'] = data_to_diff(data2[key])
        diff[key] = item
    return diff