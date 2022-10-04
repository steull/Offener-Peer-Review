import json


def separateJSON(file: json):
    """
    Load json string and in each function the string will be separated in corresponding section
    Create new json file for each section
    :param file: pass json file
    :return:
    """

    separateGenKey(file)
    separateSpatandTempKey(file)
    separateSourceKey(file)
    separateLiceKey(file)
    separateContKey(file)
    separateResoKey(file)


def separateGenKey(file: json):
    """
    Load JSON String and get only the general keys

    :param file: pass json file
    :return: General Keys as an extra file
    """

    with open(file) as json_file:
        json_data = json.loads(json_file.read())

    genKey_dict = {}

    # Add General Keys to genKey_dict
    for key, value in json_data.items():
        if key == "spatial":
            break
        genKey_dict[key] = value
        with open("files/separated_template/generalKeys.json", "w") as jsonFile:
            json.dump(genKey_dict, jsonFile, indent=4, ensure_ascii=True)


def separateSpatandTempKey(file: json):
    """
    Load JSON String and get only the general keys

    :param file: pass json file
    :return: Spatial and Temporal Keys as an extra file
    """

    with open(file) as json_file:
        json_data = json.loads(json_file.read())

    spatAndTempKey_dict = {}

    # Add Spatial and Temporal Keys to spatAndTempKey_dict
    for key, value in json_data.items():
        if key == "spatial" or key == "temporal":
            spatAndTempKey_dict[key] = value
            with open('files/separated_template/spatialAndTemporalKeys.json', 'w') as jsonFile:
                json.dump(spatAndTempKey_dict, jsonFile, indent=4, ensure_ascii=True)


def separateSourceKey(file: json):
    """
    Load JSON String and get only the general keys

    :param file: pass json file
    :return: Source Keys as an extra file
    """

    with open(file) as json_file:
        json_data = json.loads(json_file.read())

    sourceKey_dict = {}

    # Add Source Keys to sourceKey_dict
    for key, value in json_data.items():
        if key == "sources":
            sourceKey_dict[key] = value
            with open('files/separated_template/sourceKey_dict.json', 'w') as jsonFile:
                json.dump(sourceKey_dict, jsonFile, indent=4, ensure_ascii=True)


def separateLiceKey(file: json):
    """
    Load JSON String and get only the general keys

    :param file: pass json file
    :return: License Keys as an extra file
    """

    with open(file) as json_file:
        json_data = json.loads(json_file.read())

    liceKey_dict = {}

    # Add License Keys to liceKey_dict
    for key, value in json_data.items():
        if key == "licenses":
            liceKey_dict[key] = value
            with open('files/separated_template/liceKey_dict.json', 'w') as jsonFile:
                json.dump(liceKey_dict, jsonFile, indent=4, ensure_ascii=True)


def separateContKey(file: json):
    """
    Load JSON String and get only the general keys

    :param file: pass json file
    :return: Context Keys as an extra file
    """

    with open(file) as json_file:
        json_data = json.loads(json_file.read())

    contKey_dict = {}

    # Add Contributor Keys to provKey_dict
    for key, value in json_data.items():
        if key == "contributors":
            contKey_dict[key] = value
            with open('files/separated_template/contKey_dict.json', 'w') as jsonFile:
                json.dump(contKey_dict, jsonFile, indent=4, ensure_ascii=True)


def separateResoKey(file: json):
    """
    Load JSON String and get only the general keys

    :param file: pass json file
    :return: Context Keys as an extra file
    """

    with open(file) as json_file:
        json_data = json.loads(json_file.read())

    resoKey_dict = {}

    # Add Resource Keys to resoKey_dict
    for key, value in json_data.items():
        if key == "resources":
            resoKey_dict[key] = value
            with open('files/separated_template/resoKey_dict.json', 'w') as jsonFile:
                json.dump(resoKey_dict, jsonFile, indent=4, ensure_ascii=True)


separateJSON("files/template - V1.5.1.json")
