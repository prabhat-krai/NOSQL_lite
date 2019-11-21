from process_json import is_json, extract_key_value, extract_all_values, extract_values
from hashing import hash_key
from file_handling import add_file, delete_file, read_file
from index_of_db import check_for_record, add_reverse_index

def add_record_to_db(json_input, map_of_db, reverse_index):
    key, value = extract_key_value(json_input)
    value = str(value)
    if(key is not None):
        hashed_key = hash_key(key)
        value_map = extract_all_values(json_input)
        reverse_index = add_reverse_index(value_map, hashed_key, reverse_index)
        record = add_file(hashed_key)
        record.write(json_input)
        record.close()
        map_of_db[hashed_key] = True
        return map_of_db, reverse_index
    else:
        print("No key found")

def remove_record_from_db(keys, map_of_db, reverse_index):
    for key in keys:
        key = hash_key(key)
        if(check_for_record(key,map_of_db)):
            delete_file(key)
            map_of_db[key] = False
        else:
            print("Key not present in db")
    return map_of_db, reverse_index

def search_record_in_db(value, fields, map_of_db, reverse_index):
    matching_records = []
    curb_results = False
    if(len(fields)):
        curb_results = True

    for key in map_of_db:
        if(map_of_db[key]):
            value_record = read_file(key)
            for key_in_value in value_record:
                if(value_record[key_in_value] == value):
                    if(curb_results):
                        intermediary_result = []
                        for field in fields:
                            if (field in value_record):
                                intermediary_result.append(field + ":" + value_record[field])
                            else:
                                print("{} not present in record {}: ".format(field, key))
                    break
                matching_records.append(intermediary_result)

    return matching_records





    