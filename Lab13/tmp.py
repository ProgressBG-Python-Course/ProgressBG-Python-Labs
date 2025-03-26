import json

json_str = "[1,2 true]"

data = json.loads(json_str)
print(data)
