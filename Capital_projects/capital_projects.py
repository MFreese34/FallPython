# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:00:24 2019

@author: Milo
"""
import csv

def main():
    
    a_name = 'area'
    area_set = {''}
    data_items(a_name, area_set)
    
    logMalformedProject()
    unique_values()
    
def data_items(col_name, col_set):
    # open capital project file
    cap_proj_file = open('cp_data.csv', newline='')
    
    # establish list
    cp_list = []
    # establish dictionary reader
    reader = csv.DictReader(cap_proj_file)

    # delete empty value within set
    col_set.remove('')

    # add records of csv file into the list
    for row in reader:
        cp_list.append(row)

    # iterate through records in the list
    for row in cp_list:
        # Determine if item within record is already present within list
        if row[col_name] not in cp_list:
            # Determine if item is present in set and if item is blank
            if row[col_name] not in col_set and row[col_name] != '':
                # Add value to set
                col_set.add(row[col_name])
                
    # Display capital project info
    print(cp_list)
    print()
    
    # Display area values
    print('Items in area: ')
    # iterate through set
    for x in col_set:
        # Display items within set
        print(x, end = ', ')
        
    # close file
    cap_proj_file.close()

def logMalformedProject():
    
    # open capital project file
    cap_proj_file = open('cp_data.csv', newline='')
    
    # establish list
    cp_list = []
    
    # establish dictionary reader
    reader = csv.DictReader(cap_proj_file)
    
    # iterate through file
    for row in reader:
        # add records to list
        cp_list.append(row)
        
    # create txt file to write to
    with open('corrupt_data_log.txt', mode='w') as cd_log:
        # Determine if blank values are within area section of the file
        for row in cp_list:
            if row['area'] == '':
                # write the row's id value to the text file
                cd_log.write('Id:' + str(row['id']))
                cd_log.write('\n')
                
    # close files
    cd_log.close()
    cap_proj_file.close()

def unique_values():
    e_c = 'EC'
    
# Execute the main function
if __name__ == "__main__":
    main()