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
    formatted_dict[str(key.date())] = {}    #initializes the dict with a key for a specific day
    for x in range(len(value)):             #logic finds the index of the required fields such as
        item = str(value[x])                #breakfast, lunch, dinner
        if "LUNCH" in item:
            lunch_index = x
        elif "BREAKFAST" in item:
            breakfast_index = x
        elif "DINNER" in item:
            dinner_index = x
    

    breakfast = value[breakfast_index + 1: lunch_index]     #lists are made of all the items in a 
    lunch = value[lunch_index + 1: dinner_index]            #specific meal
    dinner = value[dinner_index:]
    
    breakfast = pop_restricted_items(breakfast)             #empty items and wierd '******' are removed from 
    lunch = pop_restricted_items(lunch)                     #the python lists
    dinner = pop_restricted_items(dinner)
    

    formatted_dict[str(key.date())]["BREAKFAST"] = breakfast  
    formatted_dict[str(key.date())]["LUNCH"] = lunch
    formatted_dict[str(key.date())]["DINNER"] = dinner
    

with open("task_1/menu.json", "w") as outfile: 
    json.dump(formatted_dict, outfile, indent=4)