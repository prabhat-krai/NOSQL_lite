#create record in db folder
def create_file(name):
    file_name = "./db/{}.json".format(name)
    f = open(file_name,"w+")

#delete record from db folder
def delete_file(name):
    file_name = "./db/{}.json".format(name)
    os.remove(file_name)
    
