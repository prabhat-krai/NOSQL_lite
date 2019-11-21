from .utils.process_json import is_json, extract_key_value, extract_all_values, extract_values
from .utils.hashing import hash_key
from .utils.file_handling import add_file, delete_file, read_file
from .index_of_db import check_for_record, add_reverse_index, remove_reverse_index

def add_record_to_db(json_input, map_of_db, reverse_index):
    key, value = extract_key_value(json_input) #taking key of the input to store the data with it in db
    if(key is not None):
        hashed_key = hash_key(key)  #hashing the key while storing so db can't be searched with key in folder
        value_map = extract_all_values(json_input)  #all values stored in JSON in a list
        reverse_index = add_reverse_index(value_map, hashed_key, reverse_index) #storing values with their key 
                                                                                #in a hashmap to searches faster
        record = add_file(hashed_key) #add a file in db folder with key as its name
        record.write(json_input)      #store the input JSON in the file made        
        record.close()                #close the file for the write operation 
        map_of_db[hashed_key] = True  #store in map that the key is present 
        return map_of_db, reverse_index #returning the updated map and reverse index after add operation
    else:
        print("No key found")

def remove_record_from_db(keys, map_of_db, reverse_index):
    for key in keys: #going through one key at a time
        key = hash_key(key) #hashing the key to match in map_of_db
        if(check_for_record(key,map_of_db)): #see if key is in db so it can be removed
            reverse_index = remove_reverse_index(key,reverse_index) #removing the key and its data from reverse index
            delete_file(key) #removing record from db
            map_of_db[key] = False #chaning the value to false to let the map know that entry is removed
        else:
            print("Key not present in db")
    return map_of_db, reverse_index #returning the updated map and reverse index after delete operation

def search_record_in_db(value, fields, map_of_db, reverse_index):
    all_results = []
    curb_results = False 
    if(len(fields) > 0):
        curb_results = True #if fields are provided to not send all the entries in record then curb the result to those fields
    if(value not in reverse_index):
        print("Value not present in DB")
    else:
        list_of_records = reverse_index[value] #taking all the records in which the requested value is present
        for record in list_of_records: #generating one record at a time
            record = read_file(record) #reading the data in record
            result = [] #the data we need from this record
            if(curb_results): #if user requested particular fields
                for field in fields: #going through a field at a time
                    result.append([field, extract_values(record, field)])  #extracting those field from record and appending t list
            else:
                result.append(record) #if no specific fields needed. Adding the whole record to result.
            all_results.append(result) 
        print(all_results) 





    