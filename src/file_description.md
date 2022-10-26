# File description
In src folder is the code for the local development of the Open Peer-Review. 
## separate_json.py (done)
  - Input is a OEMetadata json, and it will be divided for each category
  - Output ** are separated json files
## read_nested_files.py
  - Input  is a partly OEMetadata file (one category)
  - It reads each key, including nested lists and dicts
  - Output is a list including each key with corresponding value
  - Missing: code from comments_on_fields
## comments_on_fields.py
  - Further development and extends read_nested_files.py
  - After testing, it will be implemented in read_nested_files.py
  - Output will be another json file, which includes all comments and suggested values from the Reviewer for each key
  - Missing: show level of nested list with more dicts included
## write_in_suggestions_template.py
  - Inputs are the comments json file from the reviewer and the template for each key
  - All comments and suggested values from comments.json will be added in the template
  - The contributor can also comment in several loops on each key and compare as well as incorporate the suggested value from the reviewer. The result is also a history of the review process including all comments
  - Missing: Code to automatically identify if the reviewer or contributor added a comment, as well as a timestamp and if the suggested value from the reviewer was accepted from the contributor
## create_summary.py
  - Missing: File does not exist yet
  - Input is the created template from write_in_suggestions_template.py
  - It shall create an overview of all comments and suggested values for each key
  - Output will either be another json or just a print function which lists all comments and values
  - The goal is to send the created summary from the template back to the contributor
  - Missing: everything