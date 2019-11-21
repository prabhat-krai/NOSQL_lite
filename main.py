from db_interact import add_record_to_db, remove_record_from_db, search_record_in_db
from config import map_of_db, reverse_index
from process_json import is_json
from index_of_db import update_index

print("Command line to interact with NoSQL DB")

continue_on_cli = input("Press y to interact with db : ")

while(continue_on_cli == 'y'):
    print("Press 1 to Add a record")
    print("Press 2 to Delete a record or records by a key-value pair")
    print("Press 3 to Find all the records which contain a particular value")
    
    task_to_perform = input("Input the number corresponding to the task : ")

    if(task_to_perform == '1'):
        json_input = input("Insert a valid JSON string as input : ")
        if(is_json(json_input)):
            map_of_db, reverse_index = add_record_to_db(json_input, map_of_db, reverse_index)
        else:
            print("not a valid JSON input")

    elif(task_to_perform == '2'):
        input_keys = input("Insert the key/keys you want to delete and space seperate them : ").split()

        map_of_db, reverse_index = remove_record_from_db(input_keys, map_of_db, reverse_index)

    elif(task_to_perform == '3'):
        search_value = input("Insert the value to find all the records with : ")
        if(input("You want particular fields(press y to enter else any other alphabet)?") == 'y'):
            fields = input("Insert the fields you want and space seperate them.").split()
        else: 
            fields = []
        search_record_in_db(search_value, fields, map_of_db, reverse_index)
    else:
        print("Wrong input.")

    update_index("map_of_db",map_of_db)
    update_index("reverse_index", reverse_index)
    continue_on_cli = input("Press y to continue to interact with db : ")

print("EXIT")