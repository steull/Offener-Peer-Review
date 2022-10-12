import json

# List to ask every key in the json
key_list = []
# List to add all comments
key_comments = []


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
    ask_comment = input(f"--- Do you want to comment: '{list_of_keys}': '{value}'? "
                        f"Press 'y' or any other letter! --- ")
    if ask_comment == "y":
        comment = input(f"--- Add your comment on '{list_of_keys[len(list_of_keys) - 1]}': ")
        # !!! The key shall show all keys, if nested !!!

        ask_value_suggestion = input(f"--- Do you want to suggest a new value for: '{list_of_keys}': '{value}'? "
                                     f"Press 'y' or any other letter! --- ")
        if ask_value_suggestion == "y":
            value_suggestions = input(f"--- Add your suggested value on '{list_of_keys[len(list_of_keys) - 1]}': ")
            key_comments.append({"key": list_of_keys[len(list_of_keys) - 1],  "comment": comment,
                                 "value_suggestion": value_suggestions})
        else:
            print("--- No value suggestion added ---")
            key_comments.append({"key": list_of_keys[len(list_of_keys) - 1], "comment": comment,
                                 "value_suggestion": None})
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
        json.dump(key_comments, jsonFile, indent=4, ensure_ascii=True)


enter_dict("test_files/generalKeys.json")

"""
# Read the template
# Write comment in field 'comment'
# Write suggested_value in 'value_suggestions' (as history)
# Write suggested_value also in a copy of template

def write_suggestions_in_template():
        with open("test_files/comment_files/template_comment_on_fields.json", "w") as jsonFile:
        

"""
