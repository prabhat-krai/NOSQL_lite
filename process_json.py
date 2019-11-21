import json
def is_json(json_input):
  try:
    json_check = json.loads(json_input)
  except ValueError as e:
    return False
  return True

def extract_key_value(json_input):
    key = None
    value = None
    json_input = json.loads(json_input)
    for key_json in json_input:
        key = key_json
    if(key is not None):
        value = json_input[key]
    return key, value

def extract_values(obj, key):
    obj = json.loads(obj)
    arr = []
    def extract(obj, arr, key):
        if isinstance(obj, (dict)):
            for k, v in obj.items():
                if k == key:
                    arr.append(v)
                elif isinstance(v, (dict, list)):
                    extract(v, arr, key)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results


def extract_all_values(obj):
    obj = json.loads(obj)
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

