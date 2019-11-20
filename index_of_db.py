import json

map_of_db = json.loads(map_of_db.json)

def check_for_record(record):
    if(record in map_of_db):
        return True
    else:
        return False

def update_index():
    with open('map_of_db.json', 'w') as f:
        json.dump(map_of_db, f)
    