import json

with open('data.json', 'r') as fp:
    data = json.load(fp)

# for e in data:
#     if data[e]["suit_for_start"] == False:
#         data[e]["start_value"] = None
#     else:
#         data[e]["start_value"] = int(input("Type value for {}:".format(data[e]["name"])))

with open("codes.txt", "r") as fp:
    codes_s = fp.read()
    codes = [e[:2] for e in codes_s.split("\n")]


for e in data:
    # print(data[e])
    print("Adding cheat code for {}: {}".format(data[e]["name"], codes[int(e) - 1]).lower())
    data[e]["cheat_code"] = "01{}edd0".format(codes[int(e) - 1].lower())



with open('data.json', 'w') as fp:
    json.dump(data, fp)