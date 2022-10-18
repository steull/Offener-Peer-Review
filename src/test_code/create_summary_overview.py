import json


def enter_dict(file: json):
    with open(file) as json_file:
        json_data = json.load(json_file)
