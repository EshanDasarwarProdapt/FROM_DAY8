import json

user = {
    "id": 101,
    "name" :"ABC",
    "active" : True,
    "Skills" : ["Python", "FastApi"]
}
json_string = json.dumps(user)
print(json_string)

json_dict = json.loads(json_string)
print(json_dict)
print(json_dict['name'])
print(type(json_dict))