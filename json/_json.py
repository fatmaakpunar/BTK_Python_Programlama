import json

#cihazlar araında ortak bir veri taşıma objesi diyebiliriz
person_string = '{"name":"Fatma", "languages": ["python", "C++"]}'
#JSON string to Dict
# result = json.loads(person_string)
# result = result["name"]
# result = result["languages"]
# print(result)

# with open ("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])

person_dict = {
    "name": "Ali",
    "languages": ["Python","C#"]
}

#Dict to JSON
# result = json.dumps(person_dict)
# print(result)
# print(type(result))

# with open("person.json","w") as f:
#     json.dump(person_dict,f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent = 4, sort_keys=True)
print(person_dict)
print(result)