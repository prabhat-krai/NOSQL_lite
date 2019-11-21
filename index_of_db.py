import json 

def load_index():
    with open('map_of_db.json',"r") as json_file:
        map_of_db = json.load(json_file)
    return map_of_db

def check_for_record(record, map_of_db):
    if(record in map_of_db):
        return True
    else:
        return False

def update_index(map_of_db):
    with open('map_of_db.json', 'w') as f:
        json.dump(map_of_db, f)
    

