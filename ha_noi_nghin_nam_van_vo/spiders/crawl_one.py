import json

json_file = open('../../nom.json')
data = json.load(json_file)
print(data)