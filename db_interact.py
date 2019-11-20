from file_handling import add_file, delete_file, close_file, read_file
from process_json import extract_key_value
from index_of_db import check_for_record, load_index, update_index
from hashing import hash_key

map_of_db = load_index()

def add_record_to_db(json_input):
    key, value = extract_key_value(json_input)
    record = add_file(key)
    record.write(value)
    close_file(record)


def remove_record_from_db(keys):
    for key in keys:
        key = hash_key(key)
        if(check_for_record(key)):
            delete_file(key)
        else:
            print("Key not present in db")

def search_record_in_db(value, fields):
    matching_records = []
    curb_results = False
    if(len(fields)):
        curb_results = True

    for key in map_of_db:
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





    