import pandas as pd
import json

menu = pd.read_excel('task_1/MessMenuSample.xlsx', skiprows=[0, 12, 22])  #skipping row 0 as not required in final json

#print(menu)

formatted_dict = {}

menu_dict = menu.to_dict(orient="list")    #orient = list because it makes managing data easier

def pop_restricted_items(items):
    """Function removes elements of a list that are not wanted"""
    new_items = []
    for item in items:
        item = str(item)
        if "nan" not in item and "****" not in item:
            new_items.append(item)
    
    return new_items


for key, value in menu_dict.items():
    #print(key)
    
    for x in range(len(value)):
        item = str(value[x])
        if "LUNCH" in item:
            lunch_index = x
        elif "BREAKFAST" in item:
            breakfast_index = x
        elif "DINNER" in item:
            dinner_index = x
    
    breakfast = {"BREAKFAST": value[breakfast_index + 1: lunch_index]}
    lunch = {"LUNCH": value[lunch_index + 1: dinner_index]}
    dinner = {"DINNER": value[dinner_index:]}
    
    breakfast["BREAKFAST"] = pop_restricted_items(breakfast["BREAKFAST"])
    lunch["LUNCH"] = pop_restricted_items(lunch["LUNCH"])
    dinner["DINNER"] = pop_restricted_items(dinner["DINNER"])
    
    formatted_dict[str(key.date())] = breakfast, lunch, dinner
    

with open("task_1/menu.json", "w") as outfile: 
    json.dump(formatted_dict, outfile, indent=4)