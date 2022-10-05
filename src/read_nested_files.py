import json

# Liste, in der die einzelnen Keys abgefragt werden
key_list = []


def recall_dict(k, v):
    key_list.append(k)
    for key, value in v.items():
        key_list.append(key)
        if isinstance(value, dict):
            key_list.pop()
            recall_dict(key, value)
        elif isinstance(value, list):
            key_list.pop()
            recall_list(key, value)
        else:
            comment_key(key_list, value)
            key_list.pop()
    key_list.pop()


def recall_list(k, v):
    key_list.append(k)
    for sublist in v:
        if sublist is None:
            comment_key(key_list, v)
        else:
            for key, value in sublist.items():
                key_list.append(key)
                if isinstance(value, dict):
                    key_list.pop()
                    recall_dict(key, value)
                elif isinstance(value, list):
                    key_list.pop()
                    recall_list(key, value)
                else:
                    comment_key(key_list, value)
                    key_list.pop()
    key_list.pop()


def comment_key(list_of_keys, value):
    print(*list_of_keys, sep=" - ")
    print(f"    {value}")


def enter_dict(file: json):
    with open(file) as json_file:
        json_data = json.load(json_file)

    keyComments = {}
    for key, value in json_data.items():
        if isinstance(value, dict):
            recall_dict(key, value)
        elif isinstance(value, list):
            recall_list(key, value)
        else:
            key_list.append(key)
            comment_key(key_list, value)
            key_list.pop()


enter_dict("files/template - V1.5.1.json")
