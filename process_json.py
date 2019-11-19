def is_json(json_input):
  try:
    json_check = json.loads(json_input)
  except ValueError as e:
    return False
  return True