import json
from omi.dialects.oep.dialect import OEP_V_1_5_Dialect
from omi.dialects.oep.parser import JSONParser_1_5
from omi.dialects.oep.compiler import JSONCompilerOEM15
from omi.oem_structures.oem_v15 import OEPMetadata, Source, Timeseries

# List to ask every key in the json
key_list = []
# List to add all comments
key_comments = []


def ntest_parse_15(_input_file="files/template - V1.5.1.json"):
    with open(_input_file, "r", encoding="utf-8") as f:
        jsn = json.load(f)

        dialect15 = OEP_V_1_5_Dialect()
        parser = dialect15._parser()
        metadata = parser.parse(jsn)

        return metadata


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
    # Optional: Adjust, to print single element of list in one line
    ask_comment = input(f"--- Do you want to comment: '{list_of_keys}': '{value}'? "
                        f"Press 'y' or any other letter! --- ")
    if ask_comment == "y":
        comment = input(f"--- Add your comment on '{list_of_keys[len(list_of_keys) - 1]}': ")

        ask_value_suggestion = input(f"--- Do you want to suggest a new value for: '{list_of_keys}': '{value}'? "
                                     f"Press 'y' or any other letter! --- ")
        if ask_value_suggestion == "y":
            value_suggestions = input(f"--- Add your suggested value on '{list_of_keys[len(list_of_keys) - 1]}': ")
            # !!! The key shall show all keys, if nested !!!
            key_comments.append({"key": list_of_keys[len(list_of_keys) - 1], "comment": comment,
                                 "value_suggestion": value_suggestions})
        else:
            print("--- No value suggestion added ---")
            # !!! The key shall show all keys, if nested !!!
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


# enter_dict("test_files/generalKeys.json")


if __name__ == "__main__":
    metadata_class: OEPMetadata = ntest_parse_15()

    for key, value in metadata_class.__dict__.items():
        print(key, value, type(key), type(value))


