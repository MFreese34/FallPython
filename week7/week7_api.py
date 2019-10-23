# -*- coding: utf-8 -*-
"""
Milo Freese
Python 2
Week 7: API exercise
October 23, 2019

"""

import urllib.request
import json

###########################################
# Ensure URL is valid and get status code #
###########################################
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

######################################
# Search through recipes             #
######################################
def recipe_search():
    # iterate through available recipes by alphabet
    for i in range(ord('a'), ord('z') + 1):
        # assign numerical value
        letter = chr(i)
        
        # assign letter to be searched through meal database URL
        meal_db_data = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + letter
            
        # validate URL
        recipe_data = getResponse(meal_db_data)
    
        # determine if recipes exist for API URL and write to file
        valid_file_write(recipe_data)

############################################
# Validate recipes exist and write to file #
############################################
def valid_file_write(recipe_records):
    # Try to open file, validate that recipes exist for the given criteria
    # and write recipe record to file
    try:
        
        # Open file
        with open('recipes.txt', 'a') as meal:
            
            # iterate through record
            for i in recipe_records["meals"]:
                
                # Write fields of record to file
                meal.write(f'Category: {i["strCategory"]} | Category ID: {i["idMeal"]}')
                meal.write(f' | Meal: {i["strMeal"]} | Country Origin: {i["strArea"]}')
                meal.write('\n')
            # close file
            meal.close()
            
    # establish TypeError exception
    except TypeError:
        # close file
        meal.close()
    
######################################
# Search recipes within meal databse #
######################################
def main():
    # search through meal database api    
    recipe_search()

# Run Main function
if __name__ == '__main__':
    main()