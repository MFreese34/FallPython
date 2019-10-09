# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:01:05 2019

@author: Milo
"""
import csv
import json
LOG_FILE = 'malformedProjects.txt'
PROJECT_CSV = 'cp_data.csv'
SEARCH_FILE = 'json_text.txt'

def projectDelegator():
    proj_file = open(PROJECT_CSV, 'r')
    reader = csv.DictReader(proj_file)
    for proj in reader:
        #check for project integrity
        if check_project_integrity(proj):
            apply_project_filter(proj)
        # send well formed projects to search filter
        
def print_project_to_console(proj):
    print('***Project Profile***')
    for key in proj:
        print('Id:', proj['id'])
        print('Fiscal year:', proj['fiscal_year'])
        print('Area:', proj['area'])
        print('Asset Type:', proj['asset_type'])
        print('Status:', proj['status'])
        print()
        
def check_project_integrity(proj):
    if proj['area'] == '':
        logMalformedProject(proj['id'])
        return False
    else:
        return True
        
def logMalformedProject(projId):
    with open(LOG_FILE, 'a') as outfile:
        outfile.write(str(projId))
        outfile.write('\n')
        
def apply_project_filter(proj):
    # implement filter logic here
    # if filter outputs project, record  
    simple_json = """{
    "fiscal_year": [2018],
    "area": ["Facility Improvement"], 
    "asset_type": ["Park"], 
    "status": ["Completed", "Planned"]
    }"""
    
    search_criteria = json.loads(simple_json)
    
    for key in search_criteria:
        
        if proj[key] in search_criteria[key]:
            record_output_project(proj)
    
def record_output_project(proj):
    print_project_to_console(proj)
        
# Execute the main function
if __name__ == "__main__":
    projectDelegator()