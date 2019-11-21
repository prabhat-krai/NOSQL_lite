import json
def is_json(json_input): #checking if the input by user is valid json
  try:
    json_check = json.loads(json_input) #loading in python's JSON parser and catching if it throws exception
  except ValueError as e:
    return False
  return True

def extract_key_value(json_input): #taking the json as input and getting the key and value from it
    key = None
    value = None
    json_input = json.loads(json_input) #loading json in dictionary
    for key_json in json_input:  #if a key is present this generates it
        key = key_json
    if(key is not None):
        value = json_input[key] # value is extracted only if a key was found
    return key, value

def extract_values(obj, key): #recursive solution to find all values of a key provided
    arr = []
    def extract(obj, arr, key):
        if isinstance(obj, (dict)): #checking if dictionary
            for k, v in obj.items(): #iterating over key value pair in JSON 
                if k == key: 
                    arr.append(v) #add value as key found
                elif isinstance(v, (dict, list)):  
                    extract(v, arr, key) #recursion on list or dictionary found
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key) #if a list is present then items are generated and extract func called
        return arr

    results = extract(obj, arr, key)
    return results


def extract_all_values(obj): #works like the previous function but instead of matching to a key
    obj = json.loads(obj)    #it returns all values in the JSON
    arr = []

    def extract_values(obj, arr):
        if isinstance(obj, (dict)):
            for k, v in obj.items():
                if type(v) == str or type(v) == int:
                    arr.append(v)
                elif isinstance(v, (dict, list)):
                    extract_values(v, arr)
        elif isinstance(obj, list):
            for item in obj:
                extract_values(item, arr)
        elif isinstance(obj, str):
            arr.append(obj)
        elif isinstance(obj, int):
            arr.append(obj)
        return arr

    results = extract_values(obj, arr)
    return results

