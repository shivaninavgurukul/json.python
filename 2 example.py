# import json
# a={"lalalala": 3}
# mystring = json.dumps(a)
# print(mystring)

"json to python"
# import json
# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
# y = json.loads(x)
# the result is a Python dictionary:
# print(y["age"]) 

"python to json"
# import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y) 


import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 