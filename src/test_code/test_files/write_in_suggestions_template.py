import json


def enter_suggestion_template(file: json):
    with open(file) as json_file:
        json_data = json.load(json_file)
    return json_data


# def write_in_suggestion_template(file: json):


def new_entry(key: str, comment: str):
    templ = enter_suggestion_template("comment_files/template_comment_on_fields.json")
    key_val = key
    if key_val is templ["reviews"][0].get("key"):
        new_suggestion_entry = {"who": None,
                                "comment": comment,
                                "timestamp": None,
                                "value_suggestions": None,
                                "accepted": None}
        templ["reviews"][0].get("loop").append(new_suggestion_entry)
    else:
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

    print(templ)
    # return new_suggestion_entry


new_entry("name", "Add description")
