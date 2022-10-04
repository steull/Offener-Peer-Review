import json


def create_dict_from_json(file: json):
    with open(file) as json_file:
        json_data = json.load(json_file)

    return json_data


def iterate_over_dict(keys):
    for key, value in keys.items():
        if isinstance(value, dict):
            recall_dict(key, value)
        elif isinstance(value, list):
            recall_list(key, value)
        else:
            print(f"1: {key}: {value}")


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


"""
def write_in_json(file: json, k, l, v):
    # Create new dictionary with all added comments
    print(keyComments)
    with open("test_files/comment_files/comments.json", "w") as jsonFile:
        json.dump(keyComments, jsonFile, indent=4, ensure_ascii=True)


askComment = input(f"--- Do you want to change: '{key}': {value}'? "
                   f"Press 'y' or any other letter! ---")
if askComment == "y":
    comment = input(f"--- Add your comment on field '{key}': {value}': ")
    for kal, valu in keyComments.items():
        if kal == key:
            keyComments[kal] = comment
else:
    print("--- Next field ---")

"""

keyComments = create_dict_from_json("test_files/generalKeys.json")
iterate_over_dict(keyComments)
