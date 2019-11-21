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
    record_value = json.loads(file_name)
    print(type(record_value))
    return record_value
    
    
