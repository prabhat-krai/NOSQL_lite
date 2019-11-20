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
    value = json_input[key]

    return key, value

