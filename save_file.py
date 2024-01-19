import json

def salveFile(contacts):
    json_file_path = "contacts.json"
    
    with open(json_file_path, "w") as arquivo:
        json.dump(contacts, arquivo, indent=2)
    
    return;
    