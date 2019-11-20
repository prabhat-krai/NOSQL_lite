from hashing import hash_key, check_key
#create record in db folder
def create_file(name):
    name = hash_key(name)
    file_name = "./db/{}.json".format(name)
    f = open(file_name,"w+")
    return f

#delete record from db folder
def delete_record(name):
    file_name = "./db/{}.json".format(name)
    os.remove(file_name)

def close_record(record):
    return record.close()

def read_record(key):
    file_name = "./db/{}.json".format(name)
    record_value = json.loads(file_name)
    return record_value
    
    
