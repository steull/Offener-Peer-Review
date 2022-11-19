import json
from omi.dialects.oep.dialect import OEP_V_1_5_Dialect
from omi.dialects.oep.parser import JSONParser_1_5
from omi.dialects.oep.compiler import JSONCompilerOEM15
from omi.oem_structures.oem_v15 import OEPMetadata, Source


if __name__ == "__main__":

    file_path = "src/files/template - V1.5.1.json"
    with open(file_path, "r", encoding="utf-8") as f:
        file = f.read()

    dialect_15 = OEP_V_1_5_Dialect()

    # Oemetadata pyton object -> omi/oem_structures/oem_v15.py -> Oemetadata class
    parsed: OEPMetadata = dialect_15.parse(file)

    parsed.identifier = "hello"

    for i in parsed.sources:
        print(i)
        for u in i.licenses:
            print(u)


    # how to create a new source object
    new_source = Source(title="Test")
    review = {"comment": "abc", "suggest": Source}

    # and add it to a new metadata
    oemetadata = OEPMetadata(sources=[new_source])
    # and add to existing metadata
    parsed.sources.append(new_source)
    print(parsed)

    rendered = dialect_15.compile_and_render(parsed)
    print(rendered)

    compiled = dialect_15.compile(parsed)
    rendered = dialect_15.render(compiled)

    """
    Von Jonas:


    def ntest_parse_15(_input_file="1_test_results\metadata\metadata_v15.json"):
        with open(_input_file, "r", encoding="utf-8") as f:
            jsn = json.load(f)

            dialect15 = OEP_V_1_5_Dialect()
            parser = dialect15._parser()
            metadata = parser.parse(jsn)

            return metadata


    metadata_class: OEPMetadata = ntest_parse_15()

    for i in metadata_class.__dir__():
        if "__" not in i and not callable(getattr(metadata_class, i)):
            print(i, getattr(metadata_class, i))
    """
