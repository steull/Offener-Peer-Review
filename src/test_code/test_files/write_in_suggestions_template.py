import json


def enter_suggestion_template(file: json):
    with open(file) as json_file:
        json_data = json.load(json_file)
    return json_data


# def write_in_suggestion_template(file: json):


def new_entry(key: str, comment: str):
    templ = enter_suggestion_template("comment_files/comments_in_template_added.json")
    key_val = key
    j = 0  # Iterate over nested dicts, to get the key name
    # If dict to list all keys and corresponding comments is empty
    if not templ["reviews"]:
        new_key_and_suggestion_entry = {
            "key": key_val,
            "loop": [
                {
                    "who": None,
                    "comment": comment,
                    "timestamp": None,
                    "value_suggestions": None,
                    "accepted": None
                }
            ]
        }
        templ["reviews"].append(new_key_and_suggestion_entry)
    # If dict contain keys including another dict with at least one comment
    else:
        # Check ALL keys first, if key already exists
        # If yes, append new dict within key
        # If not, append new dict for the new key
        existing_keys = []
        for i in templ["reviews"]:
            existing_keys.append(templ["reviews"][j].get("key"))
            if templ["reviews"][j].get("key") == key_val:
                new_suggestion_entry = {"who": None,
                                        "comment": comment,
                                        "timestamp": None,
                                        "value_suggestions": None,
                                        "accepted": None}
                templ["reviews"][j].get("loop").append(new_suggestion_entry)
                j += 1
            else:
                j += 1

        if key_val not in existing_keys:
            new_key_and_suggestion_entry = {
                "key": key_val,
                "loop": [
                    {
                        "who": None,
                        "comment": comment,
                        "timestamp": None,
                        "value_suggestions": None,
                        "accepted": None
                    }
                ]
            }
            templ["reviews"].append(new_key_and_suggestion_entry)

    write_in_template(templ)


def write_in_template(comments_for_template):
    with open("comment_files/comments_in_template_added.json", "w") as jsonFile:
        json.dump(comments_for_template, jsonFile, indent=4, ensure_ascii=True)


new_entry("newDate", "Contributor: Add the correct date")
