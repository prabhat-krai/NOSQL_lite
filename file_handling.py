import os, json
from hashing import hash_key
#create record in db folder
def add_file(name):
    file_name = "./db/{}.json".format(name)
    f = open(file_name,"w+")
    return f

#delete record from db folder
def delete_file(name):
    file_name = "./db/{}.json".format(name)
    os.remove(file_name)


def read_file(name):
    file_name = "./db/{}.json".format(name)
    with open(file_name) as f:
        record_value = json.load(f)
    return record_value
    
    
