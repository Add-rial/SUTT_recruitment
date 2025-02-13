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
    formatted_dict[str(key.date())] = {}
    for x in range(len(value)):
        item = str(value[x])
        if "LUNCH" in item:
            lunch_index = x
        elif "BREAKFAST" in item:
            breakfast_index = x
        elif "DINNER" in item:
            dinner_index = x
    

    breakfast = value[breakfast_index + 1: lunch_index]
    lunch = value[lunch_index + 1: dinner_index]
    dinner = value[dinner_index:]
    
    breakfast = pop_restricted_items(breakfast)
    lunch = pop_restricted_items(lunch)
    dinner = pop_restricted_items(dinner)
    
    formatted_dict[str(key.date())]["BREAKFAST"] = breakfast
    formatted_dict[str(key.date())]["LUNCH"] = lunch
    formatted_dict[str(key.date())]["DINNER"] = dinner
    

with open("task_1/menu.json", "w") as outfile: 
    json.dump(formatted_dict, outfile, indent=4)