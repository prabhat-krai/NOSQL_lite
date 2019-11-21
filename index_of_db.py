import json, os

def load_index(name):
    file_name = "./db/{}.json".format(name)
    if(os.path.getsize(file_name) > 0):
        with open(file_name,"r") as json_file:
            index = json.load(json_file)
        return index
    else:
        return {}

def check_for_record(record, map_of_db):
    if(record in map_of_db):
        return True
    else:
        return False

def update_index(name, index):
    file_name = "./db/{}.json".format(name)
    with open(file_name, 'w') as f:
        json.dump(index, f)
    
def files_with_value(values, reverse_index):
    result = []
    for value in values:
        result.append(reverse_index[value])
    return result

def add_reverse_index(value_map, hashed_key, reverse_index):
    for value in value_map:
        if(value in reverse_index):
            reverse_index[value].append(hashed_key)
        else:
            reverse_index[value] = []
            reverse_index[value].append(hashed_key)
    
    return reverse_index
