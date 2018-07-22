import requests
import json

output = {}
for i in range(1, 152):
    r = requests.get("http://pokeapi.co/api/v2/pokemon/{}/".format(i))
    print("Attempting to connect to: http://pokeapi.co/api/v2/pokemon/{}/".format(i))
    data = r.json()

    print("Collecting data: {}".format(data["name"]))
    output[i] = {}
    output[i]["id"] = i
    output[i]["name"] = data["name"]
    type_list = []
    for e in reversed(data["types"]):
        type_list.append(e["type"]["name"])
    output[i]["all_types"] = type_list
    output[i]["main_type"] = output[i]["all_types"][0]
    output[i]["evolution"] = True
    output[i]["common"] = False
    output[i]["legendary"] = False
    output[i]["suit_for_start"] = False
    output[i]["start_value"] = None

# print(output)

with open('data.json', 'w') as fp:
    json.dump(output, fp)
