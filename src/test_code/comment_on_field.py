import json

# Liste, in der die einzelnen Keys abgefragt werden
key_list = []
# Liste, welche die Kommentare speichert
keyComments = []


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
    # !!! Adjust, to print single element of list in one line !!!
    askComment = input(f"--- Do you want to change: '{list_of_keys}': '{value}'? "
                       f"Press 'y' or any other letter! --- ")
    if askComment == "y":
        comment = input(f"--- Add your comment: ")
        # !!! The key is wrong and needs to be adjusted !!!
        keyComments.append({list_of_keys[0]: comment})
        print(keyComments)
    else:
        print("--- Next field ---")


def enter_dict(file: json):
    with open(file) as json_file:
        json_data = json.load(json_file)

    for key, value in json_data.items():
        if isinstance(value, dict):
            recall_dict(key, value)
        elif isinstance(value, list):
            recall_list(key, value)
        else:
            key_list.append(key)
            comment_key(key_list, value)
            key_list.pop()

    with open("test_files/comment_files/comments.json", "w") as jsonFile:
        json.dump(keyComments, jsonFile, indent=4, ensure_ascii=True)


enter_dict("test_files/generalKeys.json")


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
