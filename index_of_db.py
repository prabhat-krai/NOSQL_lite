import json

def load_index():
    with open('map_of_db.json',"r") as json_file:
        map_of_db = json.load(json_file)
    return map_of_db

map_of_db = load_index() 

def check_for_record(record):
    if(record in map_of_db):
        return True
    else:
        return False

def update_index():
    with open('map_of_db.json', 'w') as f:
        json.dump(map_of_db, f)

