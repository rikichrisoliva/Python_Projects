# one important note in JSON is you have to use double quotation marks, not single quotation mark like you can use Python.
# commonly used for configuration files, storing data, or APIs
import json  # built-in to the standard library of Python, no need to install it.
from typing import SupportsFloat, Union

json_data = """
{
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}
"""

data = json.loads(
    json_data
)  # the s in loads means string (not a file), to load JSON strings. You can also load a JSON file.
print(data)  # the output would be a Python dictionary, not in JSON format.
print(data["topping"][6])
print("-----------------------------------------------------------")
# dump a dictionary into JSON format
data["new_key"] = True  # just adding a new key value pair to the dictionary 'data'
new_json = json.dumps(
    data
)  # the s in dumps means string (not a file), then put the dictionary 'data' you want to dump.
print("-----------------------------------------------------------")
print(new_json)  # you should get the JSON data format
new_json = json.dumps(
    data, indent=2
)  # the s in dumps means string (not a file), then put the dictionary 'data' you want to dump.
print("-----------------------------------------------------------")
print(new_json)  # you should get the JSON data format
new_json = json.dumps(
    data, indent=4
)  # the s in dumps means string (not a file), then put the dictionary 'data' you want to dump.
print("-----------------------------------------------------------")
print(new_json)  # you should get the JSON data format
new_json = json.dumps(
    data, indent=4, sort_keys=True
)  # the s in dumps means string (not a file), then put the dictionary 'data' you want to dump.
print("-----------------------------------------------------------")
print(new_json)  # you should get the JSON data format

# in JSON, the boolean value is all lowercase - true or false. Compare to Python, the boolean value is either True or False
# Read/Open JSON data into Python dictionary
print("-----------------------------------------------------------")
with open("data.json", "r") as f:  # r means readmode. f is the object.
    data = json.load(f)  # json.load without the s because you are loading from a file.
print(data)
print("-----------------------------------------------------------")
print(data.items())
print("-----------------------------------------------------------")
print(data["batters"]["batter"][3])
print("-----------------------------------------------------------")
# How to write JSON into a file
with open("data2.json", "w") as f:  # w means writemode. f is the object.
    data = json.dump(data, f, indent=4, sort_keys=True)
