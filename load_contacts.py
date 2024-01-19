import json

def loadContacts():
    json_file_path = "contacts.json"

    with open(json_file_path, "r") as file:
        # Load the JSON data from the file
        data = json.load(file)
    
    return data
