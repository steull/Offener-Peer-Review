import json
import csv
import pathlib
from omi.dialects.oep.dialect import OEP_V_1_5_Dialect
from omi.oem_structures.oem_v15 import OEPMetadata

# Path where value_suggestions_reviewer.json will be stored
_out_json = "files/omi_output.json"
key_list = []
dialect15 = OEP_V_1_5_Dialect()


def ntest_parse_15(_input_file="files/template - V1.5.1.json"):
    with open(_input_file, "r", encoding="utf-8") as f:
        jsn = json.load(f)

        dialect15 = OEP_V_1_5_Dialect()
        parser = dialect15._parser()
        metadata = parser.parse(jsn)
        create_cont_copy(jsn)

        return metadata


def create_cont_copy(data):
    with open('files/contributor_original.json', 'w') as f:
        json.dump(data, f, indent=4)


def separateGenKey():
    metadata_class: OEPMetadata = ntest_parse_15()

    for key, value in metadata_class.__dict__.items():
        key_list.append(key)
        if key == "subject":
            lists_count = 1
            for subjectlists in value:
                for subjectkey, subjectvalue in subjectlists.__dict__.items():
                    key_list.append(subjectkey)
                    comment_key(key_list, subjectvalue, lists_count)
                    key_list.pop()
                lists_count += 1
            key_list.pop()
        elif key == "context":
            for contextkey, contextvalue in value.__dict__.items():
                key_list.append(contextkey)
                comment_key(key_list, contextvalue)
                key_list.pop()
        elif key == "spatial":
            break
        else:
            comment_key(key_list, value)
            key_list.pop()


def separateSpatandTempKey():
    """
    Load JSON String and get only the general keys

    :return: Spatial and Temporal Keys as an extra file
    """

    metadata_class: OEPMetadata = ntest_parse_15()

    # Add Spatial and Temporal Keys to spatAndTempKey_dict
    print("Spatial Keys: ")
    for k in metadata_class.spatial.__dict__.items():
        print(k)

    print("Temporal Keys: ")
    for key, value in metadata_class.temporal.__dict__.items():
        if isinstance(value, list):
            lists_count = 1
            for timeserieslists in value:
                for timekeys, timevalues in timeserieslists.__dict__.items():
                    print(lists_count, timekeys, timevalues)
                lists_count += 1
        else:
            print(key, value)


def separateSourceKey():
    """
    Load JSON String and get only the general keys

    :return: Source Keys as an extra file
    """

    metadata_class: OEPMetadata = ntest_parse_15()
    lists_count = 1

    for k in metadata_class.sources:
        for key, value in k.__dict__.items():
            if isinstance(value, list):
                for sourcelists in value:
                    for sourcekey, sourcevalue in sourcelists.__dict__.items():
                        if sourcekey == "license":
                            for licensekey, licensevalue in sourcevalue.__dict__.items():
                                print(key, sourcekey, lists_count, ":", licensekey, licensevalue)
                        else:
                            print(key, lists_count, ":", sourcekey, sourcevalue)
            else:
                print(lists_count, ":", key, value)
        lists_count += 1


def separateLiceKey():
    """
    Load JSON String and get only the general keys

    :return: License Keys as an extra file
    """
    metadata_class: OEPMetadata = ntest_parse_15()
    lists_count = 1

    for k in metadata_class.license:
        for key, value in k.__dict__.items():
            if key == "license":
                for licensekey, licensevalue in value.__dict__.items():
                    print(key, lists_count, ":", licensekey, licensevalue)
            else:
                print(lists_count, ":", key, value)
        lists_count += 1


def separateContKey():
    """
    Load JSON String and get only the general keys

    :return: Context Keys as an extra file
    """

    metadata_class: OEPMetadata = ntest_parse_15()
    lists_count = 1

    for k in metadata_class.contributions:
        for key, value in k.__dict__.items():
            if key == "contributor":
                for contkey, contvalue in value.__dict__.items():
                    print(key, lists_count, contkey, contvalue)

            else:
                print(lists_count, ":", key, value)
        lists_count += 1


def separateResoKey():
    """
    Load JSON String and get only the general keys

    :return: Context Keys as an extra file
    """

    metadata_class: OEPMetadata = ntest_parse_15()
    lists_count = 1

    for k in metadata_class.resources:
        for key, value in k.__dict__.items():
            if key == "schema":
                for schemakey, schemavalue in value.__dict__.items():
                    if schemakey == "fields":
                        for fields in schemavalue:
                            for fieldkey, fieldvalue in fields.__dict__.items():
                                if fieldkey == "isAbout":
                                    for isAbouts in fieldvalue:
                                        for isAboutkey, isAboutvalue in isAbouts.__dict__.items():
                                            print(schemakey, fieldkey, lists_count, isAboutkey, isAboutvalue)
                                elif fieldkey == "valueReference":
                                    for valueReferences in fieldvalue:
                                        for valueReferencekey, valueReferencevalue in valueReferences.__dict__.items():
                                            print(fieldkey, lists_count, valueReferencekey, valueReferencevalue)
                                else:
                                    print(key, schemakey, lists_count, fieldkey, fieldvalue)
                            lists_count += 1

            else:
                print(key, value)
        lists_count += 1


def comment_key(list_of_key: list, value, list_count=None):
    if list_count is None:
        iterate_entrances = 0
    else:
        iterate_entrances = list_count

    ask_comment = input(f"--- Do you want to comment: '{list_of_key}' on {iterate_entrances}: '{value}'? "
                        f"Press 'y' or any other letter! --- ")
    if ask_comment == "y":
        comment = input(f"--- Add your comment on '{list_of_key}' = '{value}': ")
        ask_value_suggestion = input(f"--- Do you want to suggest a new value for "
                                     f"'{list_of_key}'on {iterate_entrances}: '{value}'? "
                                     f"Press 'y' or any other letter! --- ")
        if ask_value_suggestion == "y":
            value_suggestions = input(f"--- Add your suggested value on '{list_of_key}' = '{value}': ")
            reviewer_comments_csv(list_of_key, comment, iterate_entrances, value_suggestions)
        else:
            print("--- No value suggestion added ---")
            reviewer_comments_csv(list_of_key, comment, iterate_entrances)

        return ask_value_suggestion
    else:
        print("--- Next field ---")

    return None


def mapping_metadata_omi(omi_keys: list):
    mapping_fields = {
        "identifier": "id",
        "languages": "language",
        "publication_date": "publicationDate",
        "source_code": "sourceCode",
        "grant_number": "grantNo",
        "funding_agency": "fundingAgency",
        "logo": "fundingAgencyLogo",
        "publisher": "publisherLogo",
        "reference_date": "referenceDate",
        "ts_start": "start",
        "ts_end": "end",
        "ts_resolution": "resolution",
        "ts_orientation": "alignment",
        "aggregation": "aggregationType",
        "terms_of_use": "licenses",
        "contribution": "contributions",
        "contributor": "title",
        "resource_format": "format",
        "field_type": "type",
        "primary_key": "primaryKey",
        "foreign_keys": "foreignKeys",
        "decimal_separator": "decimalSeparator"
    }

    templ_key = []
    for i in omi_keys:
        for find_key, find_val in mapping_fields.items():
            if i == find_key:
                templ_key.append(find_val)
                break
        else:
            templ_key.append(i)

    return templ_key


def reviewer_comments_csv(list_of_keys: list, comment_rev, dict_entrance=None, val_sugg_rev=None):
    templ_key = mapping_metadata_omi(list_of_keys)  # Übersetzung von omi zu Template namen
    max_entrances = 5
    new_csv_entrance = []
    list_number = len(templ_key) - 1

    for current_entrance in range(max_entrances):
        if current_entrance <= list_number:
            new_csv_entrance.append(templ_key[current_entrance])
        elif current_entrance <= max_entrances:
            new_csv_entrance.append(None)

    new_csv_entrance.append(comment_rev)
    if dict_entrance is None:
        dict_entrance = 0
        new_csv_entrance.append(dict_entrance)
    else:
        new_csv_entrance.append(dict_entrance)
    new_csv_entrance.append(val_sugg_rev)
    new_csv_entrance.append("R")
    new_csv_entrance.append("2022.11.21")

    with open('files/comments_reviewer.csv', 'a') as fi:
        data = csv.writer(fi)
        data.writerow(new_csv_entrance)
    fi.close()


def create_summary():
    pass

# Nicht genutzt: def reviewer_comments
"""
def reviewer_comments(list_of_keys: list, comment_rev, dict_entrance=None, val_sugg_rev=None):
    comments_reviewer = load_comments_reviewer("files/comments_reviewer.json")
    templ_key = mapping_metadata_omi(list_of_keys)  # Übersetzung von omi zu Template namen

    # Stelle sicher, dass du an der richtigen Stelle bist (Überprüfung aus übergebener key_list)
    # If there is no entry
    if comments_reviewer[templ_key] is None:
        first_suggestion_entry = [
            {
                "who": None,
                "comment": comment_rev,
                "timestamp": None,
                "value_suggestions": val_sugg_rev,
                "accepted": None
            }
        ]
        comments_reviewer[templ_key] = first_suggestion_entry
    # If key has already comments
    else:
        for i in dict_entrance:
            if i == dict_entrance:
                new_suggestion_entry = {"who": None,
                                        "comment": comment_rev,
                                        "timestamp": None,
                                        "value_suggestions": val_sugg_rev,
                                        "accepted": None}
                comments_reviewer[templ_key][i].append(new_suggestion_entry)
            else:
                i += 1

    save_comments_reviewer(comments_reviewer)
   """


# Wird bisher nicht genutzt!
def save_to_file(metadata: str, file_path: pathlib.Path):
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(metadata)


if __name__ == "__main__":
    metadata_class: OEPMetadata = ntest_parse_15()

    for key, value in metadata_class.__dict__.items():
        key_list.append(key)
        if key == "subject":
            lists_count = 1
            for subjectlists in value:
                for subjectkey, subjectvalue in subjectlists.__dict__.items():
                    key_list.append(subjectkey)
                    comment_key(key_list, subjectvalue, lists_count)
                    # schreibe hier an Position subjecttkey den neuen vorgeschlagenen Wert rein
                    key_list.pop()
                lists_count += 1
            key_list.pop()
        elif key == "context":
            for contextkey, contextvalue in value.__dict__.items():
                key_list.append(contextkey)
                comment_key(key_list, contextvalue)
                # schreibe hier an Position contextkey den neuen vorgeschlagenen Wert rein
                key_list.pop()
        elif key == "spatial":
            break
        else:
            comment_key(key_list, value)
            # schreibe hier an Position key den neuen vorgeschlagenen Wert rein
            key_list.pop()


    metadata_class.name = "new name"

    rendered = dialect15.compile_and_render(metadata_class)
    print(rendered)

