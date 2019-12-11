# -*- coding: utf-8 -*-
"""
December 10, 2019
Milo Freese
Python 2

Final Project: State Parks Data Simulation

"""
import pandas as pd
import matplotlib.pyplot as plt

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
            xl = ''
            if '_' in item:
                xl = item.replace('_', ' ')
                plt.xlabel(xl)
            else: 
                plt.xlabel(item)
            
            # Create y-axis label
            plt.ylabel('States')
            
            # Determine if '_' character exists in facility and format properly
            # create figure title
            sp_title = ''
            if '_' in item:
                sp_title = item.replace('_', ' ')
                plt.title('State Park ' + sp_title + ' Availability In States')
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
            xl = ''
            if '_' in item:
                xl = item.replace('_', ' ')
                plt.xlabel(xl)
            else: 
                plt.xlabel(item)
            
            # Create y-axis label
            plt.ylabel('States')
            
            # Determine if '_' character exists in facility and format properly
            # create figure title
            sp_title = ''
            if '_' in item:
                sp_title = item.replace('_', ' ')
                plt.title('State Park ' + sp_title + ' Availability In States')
            else:
                plt.title('State Park ' + item + ' Availability In States')
            
            # Show the figure
            plt.show()
            
# Close File        
f.close()