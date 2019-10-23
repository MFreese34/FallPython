# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:26:13 2019

@author: Milo
"""

import urllib.request
import json


def getResponse(url):
    # Obtain API url
    openUrl = urllib.request.urlopen(url)
    # Determine if API URL is valid
    if(openUrl.getcode()==200):
        # Read url info into variable
        data = openUrl.read()
        # Convert json string into python object
        jsonData = json.loads(data)
    else:
        # print error statement if url is invalid
        print("Error receiving data", openUrl.getcode())
        
    # Return data info
    return jsonData

def recipe_search():
    for i in range(ord('a'), ord('z') + 1):
        letter = chr(i)

        meal_db_data = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + letter
            
        recipe_data = getResponse(meal_db_data)
    
        # determine if recipes exist for API URL and write to file
        valid_file_write(recipe_data)

            
def valid_file_write(recipe_records):
    try:
        
        with open('meals1.txt', 'a') as meal:
            
            for i in recipe_records["meals"]:
                
                meal.write(f'Category: {i["strCategory"]} | Category ID: {i["idMeal"]}')
                meal.write(f' | Meal: {i["strMeal"]} | Country Origin: {i["strArea"]}')
                meal.write('\n')
                
        meal.close()
    except TypeError:
        meal.close()
    
def main():
    
    recipe_search()
"""
def apply_filter(record):
    try:
        with open('category.json', 'r') as filter1:
            filter_load = (json.load(filter1))
            
            # makes the values in filter file into strings
            criteria = {k: str(v[0]) for k,v in filter_load.items() 
                if isinstance(v, (list))} 

            if category_filter(record,criteria):
                valid_file_write(record)
    except ValueError:
        print('failed')
        
def category_filter(record,criteria):
    if record['strCategory'] == criteria['Vegetarian']:
        return True
    elif record['strCategory'] == criteria['Vegan']:
        return True
    else:
        return False
"""
if __name__ == '__main__':
    main()