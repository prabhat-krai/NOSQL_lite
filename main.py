import json 

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
            db.add_record(json_input)
        else:
            print("not a valid JSON input")

    elif(task_to_perform == '2'):
        input_key = input("Insert the key you want to delete : ")
        input_value = input("Insert the value you want to delete : ")

        db.remove_records(input_key, input_value)

    elif(task_to_perform == '3'):
        input_value = input("Insert the value to find all the records with : ")
        if(input("You want particular fields(press y to enter else any other alphabet)?") == y):
            fields = input("Insert the fields you want and space seperate them.").split()
        else: 
            fields = []
        db.find_records(input_value, fields)

    else:
        print("Wrong input.")


    continue_on_cli = input("Press y to continue to interact with db : ")
