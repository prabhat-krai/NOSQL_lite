import os, json
from hashing import hash_key
#create record in db folder
def add_file(name):
    file_name = "./db/{}.json".format(name) #creating directory name for the file 
    f = open(file_name,"w+") #creating the new file and in write mode
    return f #sending the file for write operation

#delete record from db folder
def delete_file(name):
    file_name = "./db/{}.json".format(name)  
    os.remove(file_name) #deleting file from directory location


def read_file(name):
    file_name = "./db/{}.json".format(name)
    with open(file_name) as f: 
        record_value = json.load(f) #loading the data from file to dictionary
    return record_value
    
    
