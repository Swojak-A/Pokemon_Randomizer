import json
import random

with open('data.json', 'r') as fp:
    data = json.load(fp)

def create_poke_pool(token=4, forbid_list=[]):
    your_team = []

    while token > 0:
        poke_pool = []
        print("Attempting to choose a starting pokemon for you")
        print("Remaining token: {}".format(token))
        # print(forbid_list)
        for e in data:
            if cond_start(data, e) == True and cond_type(data, e, forbid_list) == True and cond_token(data, e, token) == True:
                poke_pool.append(e)
        # print([data[x]["name"] for x in poke_pool])
        chosen_poke = random.choice(poke_pool)
        print("We've choosen pokemon to start with: {} (worth {} token/-s, cheat code: {})\n***".format(data[chosen_poke]["name"], str(data[chosen_poke]["start_value"]), data[chosen_poke]["cheat_code"]))
        your_team.append(chosen_poke)
        token -= data[chosen_poke]["start_value"]
        forbid_list.append(data[chosen_poke]["main_type"])
    print("No more tokens")
    print("Your new team is: {}".format(", ".join([data[x]["name"] + " (" + data[x]["cheat_code"] + ")" for x in your_team])))



def cond_start(data, e):
    if data[e]["suit_for_start"] == True:
        return True
    else:
        return False

def cond_type(data, e, forbid_list):
    if data[e]["main_type"] not in forbid_list:
        return True
    else:
        return False

def cond_token(data, e, token):
    if data[e]["start_value"] <= token:
        return True
    else:
        return False



if __name__ == "__main__":
    create_poke_pool(token=2)