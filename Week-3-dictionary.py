# -*- coding: utf-8 -*-
"""

Milo Freese
Python 2
Week 3 Dictionary
September 18, 2019
Modified September 20 by Lisa Nydick to add Error Handling and more consistant prompts

"""
import sys
Global_Data = {'North America': 
                    {'Antigua and Barbuda': 
                        {'Population': '96,286',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Bahamas':
                        {'Population': '',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Belize':
                        {'Population': '383,071',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Canada':
                        {'Population': '37,058,856',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Costa Rica':
                        {'Population': '4,999,441',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Cuba':
                        {'Population': '11,338,138',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Dominica':
                        {'Population': '71,625',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Dominican Republic':
                        {'Population': '10,627,165',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'El Salvador':
                        {'Population': '6,420,764',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Grenada':
                        {'Population': '111,454',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Guatemala':
                        {'Population': '17,247,807',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Haiti':
                        {'Population': '11,123,176',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Honduras':
                        {'Population': '9,587,522',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Jamaica':
                        {'Population': '2,934,855',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Mexico':
                        {'Population': '126,190,788',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Nicaragua':
                        {'Population': '6,465,513',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Panama':
                        {'Population': '4,176,873',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Trinidad and Tobago':
                        {'Population': '1,389,858',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'United States of America':
                        {'Population': '327,167,434',
                         'GDP': '',
                         'CO2 Emissions': ''}},
                'Australia':
                    {'Australia':
                        {'Population': '24,992,369',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Fiji':
                        {'Population': '883,483',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Kiribati':
                        {'Population': '115,847',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Marshall Islands':
                        {'Population': '58,413',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Micronesia':
                        {'Population': '112,640',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Nauru':
                        {'Population': '12,704',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'New Zealand':
                        {'Population': '4,885,500',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Palau':
                        {'Population': '17,907',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Papua New Guinea':
                        {'Population': '8,606,316',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Samoa':
                        {'Population': '196,130',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Solomon Islands':
                        {'Population': '652,858',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Tonga':
                        {'Population': '103,197',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Tuvalu':
                        {'Population': '11,508',
                         'GDP': '',
                         'CO2 Emissions': ''},
                    'Vanuatu':
                        {'Population': '292,680',
                         'GDP': '',
                         'CO2 Emissions': ''}}}

#Message Global Const
ERROR = "ERROR:"
ERROR_INVALID_SELECTION = 'ERROR: Invalid selection.  Please enter a valid option.'
ERROR_KEY_NOT_FOUND = "Not Found.  Values are case-sensitive."
ERROR_KEY_ALREADY_EXISTS = "Already Exists."

ENTER = "Enter a "
COUNTRY = "Country"
CONTINENT = "Continent"
DEMOGRAPHIC = "Demographic"
DEMOGRAPHIC_VALUE = "Demographic Value"
KEY_FOUND = 'Key Found'

def main():
    display_menu = True
    
    while display_menu == True:     #Loop until user enters a valid selection
        # Display user available options
        print('                  Options')
        print('--------------------------------------------')
        print('1) Display Continents')
        print('2) Display Countries')
        print('3) Display Demographics of Specified Country')
        print('4) Delete an Item')
        print('5) Add an Item')
        print('6) End Program')
       
        #Catch error where user enters a non-numeric value
        try:
            user_input = int(input('Enter numerical selection: '))
            
            # Determine user input selection
            if user_input == 1:            
                # Display Continent Info
                print()
                display_continents()
                print()
                display_menu = False    #Input was valid, so stop looping
                main()
        
            elif user_input == 2:        
                # Display Country Info
                print()
                display_countries()
                print()
                display_menu = False
                main()
        
            elif user_input == 3:   
                # Display Demographic info
                print()
                display_countries_demographics()
                print()
                display_menu = False
                main()
            elif user_input == 4:
                # Provide user option to delete an item from dictionary
                print()
                delete()
                print()
                display_menu = False
                main()
            elif user_input == 5:
                # Provide user an option to add an item to dicionary
                print()
                add()
                print()
                display_menu = False
                main()
            elif user_input == 6:
                # Terminate Program
                display_menu = False
                sys.exit
            else:
                print()
                print(ERROR_INVALID_SELECTION)
                print()
                display_menu = True     #Keep looping
        except Exception as err:
            if str(err).find('invalid literal') != -1:  #Error converting string to int type
                print()
                print(ERROR_INVALID_SELECTION)
                print()
                display_menu = True     #Keep looping
            else:
                print()
                print(err)
                print()
                display_menu = True     #Keep looping



def display_continents():
    
    # Display Continents within dictionary
    for continent in Global_Data: 
        print(continent) 
    
def display_countries():
    keyfound = False
    # Obtain user input
    continent_input = input(ENTER + CONTINENT + ':')
    print()
    
    #Make sure the input is a valid key
    keyfound = find_key(Global_Data, continent_input)
    if keyfound == True:
        # Display Countries within dictionary
        for country in Global_Data[continent_input]: 
            print(country)
    else:   #Key was not found
        print(ERROR + ' ' + CONTINENT + ' "' + continent_input + '" ' + ERROR_KEY_NOT_FOUND)

    
def display_countries_demographics():
    key1found = False
    key2found = False

    # Obtain user input
    continent_input = input(ENTER + CONTINENT + ':')
    
    #Make sure the input is a valid key
    key1found = find_key(Global_Data, continent_input)
    if key1found == True: 
        country_input = input(ENTER + COUNTRY + ':')

        #Make sure the input is a valid key
        key2found = find_key(Global_Data[continent_input], country_input)
        if key2found == True:
            # Display specified country demographics
            print(Global_Data[continent_input][country_input])
        else:   #Key was not found
            print(ERROR + ' ' + COUNTRY + ' "' + country_input + '" ' + ERROR_KEY_NOT_FOUND)
    else:   #Key was not found
        print(ERROR + ' ' + CONTINENT + ' "' + continent_input + '" ' + ERROR_KEY_NOT_FOUND)
    
def delete():
    key1found = False
    key2found = False
    key3found = False
    display_menu = True
    
    # Obtain user input
    continent_input = input(ENTER + CONTINENT + ':')
    #Make sure the input is a valid key
    key1found = find_key(Global_Data, continent_input)
    if key1found == True:
    
        del_item = input('Delete a country or demographic? [C = Country, ' +
                                           'D = Demographic]: ')
        
        while display_menu == True:     #Keep displaying menu until a valid option is entered
            # Determine if user selected to delete country item
            if 'C' in del_item:
                display_menu = False    #Stop looping
                # Obtain user input
                country_input = input(ENTER + COUNTRY + ':')
                
                #Make sure the input is a valid key
                key2found = find_key(Global_Data[continent_input], country_input)
                if key2found == True:                
                    # Delete item
                    del Global_Data[continent_input][country_input]
                else:
                    print(ERROR + ' ' + COUNTRY + ' "' + country_input + '" ' + ERROR_KEY_NOT_FOUND)
                
                
            # Determine if user selected to delete demographic item
            elif 'D' in del_item:
                display_menu = False    #Stop looping
                # Obtain user input
                country_input = input(ENTER + COUNTRY + ':')
                
                #Make sure the input is a valid key
                key2found = find_key(Global_Data[continent_input], country_input)
                if key2found == True:                
                    demo_input = input(ENTER + DEMOGRAPHIC + ':')
                    
                    #Make sure the input is a valid key
                    key3found = find_key(Global_Data[continent_input][country_input], demo_input)
                    if key3found == True:
                        # Delete item
                        del Global_Data[continent_input][country_input][demo_input]
                    else:
                        print(ERROR + ' ' + DEMOGRAPHIC + ' "' + demo_input + '" ' + ERROR_KEY_NOT_FOUND)
                else:
                    print(ERROR + ' ' + COUNTRY + ' "' + country_input + '" ' + ERROR_KEY_NOT_FOUND)
                
            else:
                #Invalid selection.  Keep looping.
                print(ERROR_INVALID_SELECTION)
                display_menu = True
    else:   #Key was not found
        print(ERROR + ' ' + CONTINENT + ' "' + continent_input + '" ' + ERROR_KEY_NOT_FOUND)
    
def add():
    key1found = False
    key2found = False
    key3found = False


    display_menu = True
    
    while display_menu == True:     #Loop until user enters a valid selection
    
        # Display selections
        print('   Addition Selections')
        print('--------------------------')
        print('1) Add a Continent')
        print('2) Add a Country')
        print('3) Add a Demographic')
        print('4) Add a Demographic Value')
    
        try:    #catch error where user enters a non-numeric value
            user_input = int(input('Enter numerical selection: '))
    
            # Determine user input selection
            if user_input == 1:     #Add Continent
                display_menu = False    #Input was valid, so stop looping
        
                # Obtain user input 
                continent_input = input(ENTER + CONTINENT + ':')
            
                #Make sure the doesn't already exist
                key1found = find_key(Global_Data, continent_input)
                
                if key1found == False:        
                    # Add input into dictionary
                    Global_Data[continent_input] = {}
                    
                else:
                    print(ERROR + ' ' + CONTINENT + ' "' + continent_input + '" ' + ERROR_KEY_ALREADY_EXISTS)
                    
        
            elif user_input == 2:   #Add Country
                display_menu = False
        
                # Obtain user input
                continent_input = input(ENTER + CONTINENT + ':')
                
                #Make sure the input is a valid key
                key1found = find_key(Global_Data, continent_input)

                if key1found == True:        
                    # Obtain user input
                    country_input = input(ENTER + COUNTRY + ':')

                    #Make sure the doesn't already exist
                    key2found = find_key(Global_Data[continent_input], country_input)
                    if key2found == False:
                        # Add input into dictionary
                        Global_Data[continent_input][country_input] = {}
                    else:   #Key already exists, so it can't be added
                        print(ERROR + ' ' + COUNTRY + ' "' + country_input + '" ' + ERROR_KEY_ALREADY_EXISTS)
                else:   #Key was not found
                    print(ERROR + ' ' + CONTINENT + ' "' + continent_input + '" ' + ERROR_KEY_NOT_FOUND)

        
            elif user_input == 3:   #Add Demographic
                display_menu = False
        
                # Obtain user input
                continent_input = input(ENTER + CONTINENT + ':')
                
                #Make sure the input is a valid key
                key1found = find_key(Global_Data, continent_input)
                if key1found == True: 
                    #Obtain user input
                    country_input = input(ENTER + COUNTRY + ':')
                
                    #Make sure the input is a valid key
                    key2found = find_key(Global_Data[continent_input], country_input)
                    if key2found == True:
                        # Obtain user input
                        demo_input = input(ENTER + DEMOGRAPHIC + ':')  
                    
                        #Make sure the key doesn't already exist
                        key3found = find_key(Global_Data[continent_input][country_input], demo_input)
                        if key3found == False:
                            # Add input into dictionary
                            Global_Data[continent_input][country_input][demo_input] = {}
                        else:   #Key already exists, so it can't be added
                            print(ERROR + ' ' + DEMOGRAPHIC + ' "' + demo_input + '" ' + ERROR_KEY_ALREADY_EXISTS)
                    else:
                        print(ERROR + ' ' + COUNTRY + ' "' + country_input + '" ' + ERROR_KEY_NOT_FOUND)
                else:
                    print(ERROR + ' ' + CONTINENT + ' "' + continent_input + '" ' + ERROR_KEY_NOT_FOUND)                        

            
            elif user_input == 4:   #Add Demographic Value
                display_menu = False
                # Obtain user input
                continent_input = input(ENTER + CONTINENT + ':')

                #Make sure the input is a valid key
                key1found = find_key(Global_Data, continent_input)
                if key1found == True: 
                    #Obtain user input
                    country_input = input(ENTER + COUNTRY + ':')
                
                    #Make sure the input is a valid key
                    key2found = find_key(Global_Data[continent_input], country_input)
                    if key2found == True:
                        # Obtain user input
                        demo_input = input(ENTER + DEMOGRAPHIC + ':')            
    
                        #Make sure the input is a valid key
                        key3found = find_key(Global_Data, continent_input)
                        if key3found == True:     

                            #Obtain user input
                            value_input = input(ENTER + DEMOGRAPHIC_VALUE + ':') 
                            
                            # Add input into dictionary
                            Global_Data[continent_input][country_input][demo_input] = value_input
                        else:
                            print(ERROR + ' ' + DEMOGRAPHIC + ' "' + demo_input + '" ' + ERROR_KEY_NOT_FOUND)                        
                       
                    else:
                        print(ERROR + ' ' + COUNTRY + ' "' + country_input + '" ' + ERROR_KEY_NOT_FOUND)                    
                else:
                    print(ERROR + ' ' + CONTINENT + ' "' + continent_input + '" ' + ERROR_KEY_NOT_FOUND)                        

            else:   #Invalid selection
                print()
                print(ERROR_INVALID_SELECTION)
                print()
                display_menu = True
        except Exception as err:
            if str(err).find('invalid literal') != -1:  #Error converting string to int type
                print()
                print(ERROR_INVALID_SELECTION)
                print()
                display_menu = True
            else:
                print()
                print(err)
                print()
                display_menu = True            

# Function makes sure a user-input key exists in the dictionary
def find_key(d, key):
    v = ''
    v = d.get(key, ERROR_KEY_NOT_FOUND)

    if v == ERROR_KEY_NOT_FOUND:
        return False
    else:
        return True
    
# Execute the main function
if __name__ == "__main__":
    main()