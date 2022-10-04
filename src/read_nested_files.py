import json


def recall_dict(k, v):
    for key, value in v.items():
        if isinstance(value, dict):
            recall_dict(key, value)
        elif isinstance(value, list):
            recall_list(key, value)
        else:
            print(f"2: '{k}'-->{key}: {value}")


def recall_list(k, v):
    for sublist in v:
        if sublist is None:
            print(f"3: {k}: {v}")
        else:
            for key, value in sublist.items():
                if isinstance(value, dict):
                    recall_dict(key, value)
                elif isinstance(value, list):
                    recall_list(key, value)
                else:
                    print(f"4: '{k}'--> {key}: {value}")


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
            print(f"1: {key}: {value}")


enter_dict("files/template - V1.5.1.json")
