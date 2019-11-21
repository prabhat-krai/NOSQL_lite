import json, os

def update_index(name, index): 
    file_name = "./db/{}.json".format(name) 
    with open(file_name, 'w') as f:
        json.dump(index, f) #dumping the dictionary in json to keep metadata of db

def load_index(name): #loading data in map and reverse index at the start of the program
    file_name = "./db/{}.json".format(name)  #directory name
    if(os.path.getsize(file_name) > 0): #checking if file has data
        with open(file_name,"r") as json_file:
            index = json.load(json_file) #loading data in a dictionary
        return index
    else:
        return {} #empty dictionary if file is empty

def check_for_record(record, map_of_db):
    if(record in map_of_db): #check if the record is in map of db
        return True
    else:
        return False
    
def files_with_value(values, reverse_index): #using reverse index to get all the files with a value
    result = [] 
    for value in values: 
        result.append(reverse_index[value])
    return result

def add_reverse_index(value_map, hashed_key, reverse_index): #on adding a record taking all the values and 
    for value in value_map:                                  #creating an index for fast search
        if(value in reverse_index): #if value is present
            reverse_index[value].append(hashed_key) #append to already present hash mapping
        else: #if not present
            reverse_index[value] = [] #create the hash map
            reverse_index[value].append(hashed_key) #and append to it
    
    return reverse_index

def remove_reverse_index(key, reverse_index): #on deleting a record
    for entry in reverse_index:               #remove mappings from reverse index
        list_of_keys = reverse_index[entry]
        list_of_keys = list(filter(lambda a: a != key, list_of_keys)) #removing all key occurances
        reverse_index[entry] = list_of_keys 

    return reverse_index #updated reverse index