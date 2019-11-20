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
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results
