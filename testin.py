import json

data_blob = '''{
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
	"toppings":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		],
    "baking_method":
		[
			{ "id": "1001", "type": "Oven" }
		],
    "price_info":
		[
			{ "id": "5001", "price": "2.25", "unit": "ea" },
			{ "id": "5002", "price": "2.25", "unit": "ea" },
			{ "id": "5005", "price": "2.25", "unit": "ea" },
			{ "id": "5007", "price": "1.99", "unit": "ea" },
			{ "id": "5006", "price": "2.19", "unit": "ea" },
			{ "id": "5003", "price": "1.59", "unit": "ea" },
			{ "id": "5004", "price": "2.45", "unit": "ea" }
		]
}'''

# Create an empty list
partner_list = []

# Convert the JSON blob to a Python dictionary
data = json.loads(data_blob)
for item in data:
    name = data["name"]
    batter = data["batters"]["batter"][0]["id"]

    cake = {"name": name, "batters" : batter}

print(f' {cake} '  )

# Print just the ID of the first topping in the first entry
#print(f' { data_json["name"], data_json["batters"]["batter"][0]["type"][0] }')

# Print the first entry in the "topping" list
# Lists are ordered, dictionaries are not, numbering starts at zero
#print(data_json["toppings"][0])
# Print the third entry in the list
#print(data_json["toppings"][2])

# if len(data_json["baking_method"]) == 1:
#     print('There is 1 baking method.')
# else:
#     print(f'There are { len(data_json["baking_method"]) } baking methods.')