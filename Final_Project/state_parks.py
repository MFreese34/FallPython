# -*- coding: utf-8 -*-
"""
December 10, 2019
Milo Freese
Python 2

Final Project: State Parks Data Simulation

"""
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import time

# Establish URL constant variable
BASECAMP = 'http://www.gpsbasecamp.com/state-parks/'
    
#####################
#       Main        #
#####################
def main():

    # Declare states list
    states = []
    # Call get_states to obtain list of states from website
    states = get_states(states)
    
    # Declare dictionary
    state_park_data = { }
    
    # Call states_data to obtain state park and facility count,
    # and to assign values to state_park_data dictionary
    state_park_data = states_data(states, state_park_data)    
    
    # Run data simulation
    stats()

##################################
# State Park Syntax Correction   #
##################################
def park_synt(state_park):
    park_syntax = ''
    # determine if space exists within state park name
    if ' ' in state_park:
        # replace space with proper web address syntax
        park_syntax = state_park.replace(' ', '_')
    else:
        # assign state park name to park_syntax var
        park_syntax = state_park
        
    return park_syntax

#############################
# State Syntax Correction   #
#############################
def state_synt(state):
    st_synt = ''
    if ' ' in state:
        st_synt = state.replace(' ', '_')
    else:
        st_synt = state
    
    return st_synt

#############################
# Get State Names into list #
#############################
def get_states(states):
    
    # Call url_request to obtain website search response
    response = urllib.request.urlopen(BASECAMP)
    
    # Get HTML from website
    html = BeautifulSoup(response, 'html.parser')
    
    # find all appropriate <a> tages
    for tag in html.findAll('a'):
        # Only select tags relevant to states that have state parks
        if 'state-park' in tag['href']:
            # Exclude irrelevent HTML
            if 'State Parks' not in tag.text:
                # Convert type to string and add states to list
                states.append(str(tag.text))

    # Return states list
    return states

#####################
# State HTML Search #
#####################
def st_search(html, st_list):
    # find all appropriate <a> tages
    for tag in html.findAll('a'):
        # Only select tags relevant to states that have state parks
        if 'state-park' in tag['href']:
            # Exclude irrelevent HTML
            if 'State Parks' not in tag.text:
                # Convert type to string and add states to list
                st_list.append(str(tag.text))
                
    # Return states list
    return st_list

######################################################
# Input Variables: States list, States Dictionary    #
# Output Variables: States Dictinary                 #
# Perform operations to obtain state park count,     # 
# to obtain state park facilities count and assign   #
# values to the States Dictionary                    #
###################################################### 
def states_data(states, st_dic):
    state_parks = [] # establish individual state park list
    park_count = 0   # initialize park count
    record = 1       # Initialize dictionary record count
    st_synt = ''     # initialize state web address syntax

    # iterate through states to determine state park count and add state
    # parks to list
    for state in states:
        # Determine if space exists within state name
        st_synt = state_synt(state)
        
        # concatenate web address with state name to url var
        url = BASECAMP + st_synt
        # obtain website resopnse
        response = urllib.request.urlopen(url)
        # obtain html from state web address
        html = BeautifulSoup(response, 'html.parser')
        # search through all <a> tags
        for tag in html.findAll('a'):
            # Determine if state name is within tag and exclude unnecessary info
            if state in tag['href'] and 'map' not in tag['href']:
                # increment state park count
                park_count += 1
                # add state park name to list
                state_parks.append(tag['title'])
        # initialize state name to dictionary
        st_dic[record] = {}
        #spc[state] = {}
        st_dic[record]['State'] = state
        # add state park count key/value to dictionary
        st_dic[record]['State_Park_Count'] = park_count
        
        # Reset state park count to zero
        park_count = 0
        
        for park in state_parks:
            
            # Establish state park website syntax
            sp_synt = ''
            # Call park_synt to 
            sp_synt = park_synt(park)
            
            # Replace space within state name with proper web address syntax
            st_syntax = state.replace(' ', '%20')
            
            # concatenate web address with state and state park syntax
            park_url = BASECAMP + st_syntax + '/' + sp_synt
            
            # Obtain response from state park web address
            response = urllib.request.urlopen(park_url)
    
            # obtain html from state park web address
            html = BeautifulSoup(response, 'html.parser')
            
            # search for <img> tags within html
            for tag in html.findAll('img'):
                # assign facility name to variable
                facility = tag.get('title')
                # Determine if the facility is available within state park
                if 'Not available' in str(facility):
                    
                    # Determine if phrase exists within facility
                    # Replace whitespace with '_'
                    adj_facility = facility.replace(' Not available', '')
                    adj_facility = adj_facility.replace(' ', '_')
                    
                    # Determine if record exists within the keys
                    # Assign record to value of zero if it doesn't exist
                    if adj_facility in st_dic[record].keys():
                        adj_facility = adj_facility
                    else: 
                        st_dic[record][adj_facility] = 0
                        
                elif 'Availability unknown' in str(facility):
                    # Determine if phrase exists within facility name
                    # Replace whitespace with '_'
                    adj_facility = facility.replace(' Availability unknown', '')
                    adj_facility = adj_facility.replace(' ', '_')
                    
                    # Determine if record already exists within key
                    # assign value of zero to record if it does not exists
                    if adj_facility in st_dic[record].keys():
                        adj_facility = adj_facility
                    else: 
                        st_dic[record][adj_facility] = 0
                
                elif 'Available' in str(facility):
                    # Determine if phrase exists within facility name
                    # replace whitespace with '_'
                    adj_facility = facility.replace(' Available', '')
                    adj_facility = adj_facility.replace(' ', '_')
                    
                    # Determine if facility already exists within dictionary
                    if adj_facility in st_dic[record].keys():
                        
                        # increment value of facility key in dictionary
                        st_dic[record][adj_facility] += 1
                        
                    # Assign facility key to dictionary and assign value of 1
                    else:
                        st_dic[record][adj_facility] = 1
        
        print(st_dic[record])
        
        # Write state record to csv file
        pd.DataFrame.from_dict(data=st_dic, orient='index').to_csv('sp_data.csv')   
        
        # Increment record
        record += 1
        
        # Allow for gap time between website responses
        time.sleep(30)

    # Return dictionary
    return st_dic

#############################
# Run Data Simulation       #
#############################
def stats():
    # Establish pandas dataframe 
    df = pd.read_csv("state_parks_data.csv")
    
    # Open file and write title
    f = open("state_parks_stats.txt", "a")
    f.write('United States State Park Statistics')
    f.write('\n-----------------------------------\n\n')
    
    for item in df:
        if 'Unnamed: 0' not in item: 
            if 'State' not in item:
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                total = df[item].sum()
                
                t_val = '' # Establish format var 
    
                if '_' in item:
                    t_val = item.replace('_', ' ')
    
                    f.write('Total ' + str(t_val) + ': ' + str(total))
                    f.write('\n')
                else:
                    f.write('Total ' + str(item) + ': ' + str(total))
                    f.write('\n')
                    
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                average = df[item].mean()
                
                a_val = '' # Establish format var 
                
                if '_' in item:
                    a_val = item.replace('_', ' ')
                    f.write('Average ' + str(a_val) + ': ' + str(average))
                    f.write('\n')
                else:
                    f.write('Average ' + str(item) + ': ' + str(average))
                    f.write('\n')
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                maxx = df[item].max()
                
                m_val = '' # Establish format var 
                
                if '_' in item:
                    m_val = item.replace('_', ' ')
                    f.write('Max ' + str(m_val) + ': ' + str(maxx))
                    f.write('\n')
                else:
                    f.write('Max ' + str(item) + ': ' + str(maxx))
                    f.write('\n')
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                minn = df[item].min()
                
                mi_val = '' # Establish format var 
                
                if '_' in item:
                    mi_val = item.replace('_', ' ')
                    f.write('Min ' + str(mi_val) + ': ' + str(minn))
                    f.write('\n\n')
                else:
                    f.write('Min ' + str(item) + ': ' + str(minn))
                    f.write('\n\n')
                
                # Establish x (state park facility) and y (state) variables
                x = df[item]
                y = df.State
                
                # Establish figure and axes
                fig, ax = plt.subplots(figsize=(7, 15))
                
                # assign x,y values to figure, make plot graph, 
                # assign markers and color
                ax.plot(x,y, marker = 'o', color = 'green')
                
                # Determine if '_' character exists in facility and format properly
                # create x-axis label
                if '_' in item:
                    item = item.replace('_', ' ')
                    plt.xlabel(item)
                else: 
                    plt.xlabel(item)
                
                # Create y-axis label
                plt.ylabel('States')
                
                # Determine if '_' character exists in facility and format properly
                # create figure title
                if '_' in item:
                    item = item.replace('_', ' ')
                    plt.title('State Park ' + item + ' Availability In States')
                else:
                    plt.title('State Park ' + item + ' Availability In States')
                
                # Show the figure
                plt.show()
                
                
            if 'State_' in item:
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                total = df[item].sum()
                
                t_val = '' # Establish format var 
    
                if '_' in item:
                    t_val = item.replace('_', ' ')
    
                    f.write('Total ' + str(t_val) + ': ' + str(total))
                    f.write('\n')
                else:
                    f.write('Total ' + str(item) + ': ' + str(total))
                    f.write('\n')
                    
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                average = df[item].mean()
                
                a_val = '' # Establish format var 
                
                if '_' in item:
                    a_val = item.replace('_', ' ')
                    f.write('Average ' + str(a_val) + ': ' + str(average))
                    f.write('\n')
                else:
                    f.write('Average ' + str(item) + ': ' + str(average))
                    f.write('\n')
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                maxx = df[item].max()
                
                m_val = '' # Establish format var 
                
                if '_' in item:
                    m_val = item.replace('_', ' ')
                    f.write('Max ' + str(m_val) + ': ' + str(maxx))
                    f.write('\n')
                else:
                    f.write('Max ' + str(item) + ': ' + str(maxx))
                    f.write('\n')
                
                # Establish sum of facility column to var
                # Determine if '_' exists in value name and format
                # Write facility and value to file
                minn = df[item].min()
                
                mi_val = '' # Establish format var 
                
                if '_' in item:
                    mi_val = item.replace('_', ' ')
                    f.write('Min ' + str(mi_val) + ': ' + str(minn))
                    f.write('\n\n')
                else:
                    f.write('Min ' + str(mi_val) + ': ' + str(minn))
                    f.write('\n\n')
                
                # Establish x (state park facility) and y (state) variables
                x = df[item]
                y = df.State
                
                # Establish figure and axes
                fig, ax = plt.subplots(figsize=(7, 15))
                
                # assign x,y values to figure, make plot graph, 
                # assign markers and color
                ax.plot(x,y, marker = 'o', color = 'green')
                
                # Determine if '_' character exists in facility and format properly
                # create x-axis label
                if '_' in item:
                    item = item.replace('_', ' ')
                    plt.xlabel(item)
                else: 
                    plt.xlabel(item)
                
                # Create y-axis label
                plt.ylabel('States')
                
                # Determine if '_' character exists in facility and format properly
                # create figure title
                if '_' in item:
                    item = item.replace('_', ' ')
                    plt.title('State Park ' + item + ' Availability In States')
                else:
                    plt.title('State Park ' + item + ' Availability In States')
                
                # Show the figure
                plt.show()
                
    # Close File        
    f.close()
    
# Execute the main function
if __name__ == "__main__":
    main()