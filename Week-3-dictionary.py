# -*- coding: utf-8 -*-
"""

Milo Freese
Python 2
Week 3 Dictionary
September 18, 2019

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
def main():
    
    # Display user available options
    print('                  Options')
    print('--------------------------------------------')
    print('1) Display Continents')
    print('2) Display Countries')
    print('3) Display Demographics of Specified Country')
    print('4) Delete an Item')
    print('5) Add an Item')
    print('6) End Program')
    user_input = int(input('Enter numerical selection: '))

# Determine user input selection
    if user_input == 1:            
        # Display Continent Info
        print()
        display_continents()
        print()
        main()
        
    elif user_input == 2:        
        # Display Country Info
        print()
        display_countries()
        print()
        main()
        
    elif user_input == 3:   
        # Display Demographic info
        print()
        display_countries_demographics()
        print()
        main()
    elif user_input == 4:
        # Provide user option to delete an item from dictionary
        print()
        delete()
        print()
        main()
    elif user_input == 5:
        # Provide user an option to add an item to dicionary
        print()
        add()
        print()
        main()
    elif user_input == 6:
        # Terminate Program
        sys.exit

def display_continents():
    
    # Display Continents within dictionary
    for continent in Global_Data: 
        print(continent) 
    
def display_countries():
    
    # Obtain user input
    continent_input = input('Enter a Continent: ')
    print()
    
    # Display Countries within dictionary
    for country in Global_Data[continent_input]: 
        print(country)
    
def display_countries_demographics():
    
    # Obtain user input
    continent_input = input('Enter a Continent: ')
    country_input = input('Enter a Country: ')
    print()
    
    # Display specified country demographics
    print(Global_Data[continent_input][country_input])
        
def delete():
    
    # Obtain user input
    cont_input = input('Continent: ')
    del_item = input('Delete a country or demographic? [C = Country, ' +
                                           'D = Demographic]: ')
    
    # Determine if user selected to delete country item
    if 'C' in del_item:
        
        # Obtain user input
        country_input = input('Country: ')
        # Delete item
        del Global_Data[cont_input][country_input]

        
    # Determine if user selected to delete demographic item
    elif 'D' in del_item:
        
        # Obtain user input
        country_input = input('Country: ')
        demo = input('Demographic: ')
        # Delete item
        del Global_Data[cont_input][country_input][demo]
    
def add():

    # Display selections
    print('   Addition Selections')
    print('--------------------------')
    print('1) Add a Continent')
    print('2) Add a Country')
    print('3) Add a Demographic')
    print('4) Add a Demographic Value')
    user_input = int(input('Enter numerical selection: '))
    
# Determine user input selection
    if user_input == 1:
        
        # Obtain user input 
        cont_input = input('Enter Continent: ')
        # Add input into dictionary
        Global_Data[cont_input] = {}
        
    elif user_input == 2:
        
        # Obtain user input
        cont_input = input('Enter Continent: ')
        country_input = input('Enter Country: ')
        # Add input into dictionary
        Global_Data[cont_input][country_input] = {}
        
    elif user_input == 3:
        
        # Obtain user input
        cont_input = input('Enter Continent: ')
        country_input = input('Enter Country: ')
        demo_input = input('Enter Demographic: ')
        # Add input into dictionary
        Global_Data[cont_input][country_input][demo_input] = {}
        
    elif user_input == 4:
        
        # Obtain user inputcont_input = input('Enter Continent: ')
        cont_input = input('Enter Continent: ')
        country_input = input('Enter Country: ')
        demo_input = input('Enter Demographic: ')
        value_input = input('Enter Demographic Value: ')
        # Add input into dictionary
        Global_Data[cont_input][country_input][demo_input] = value_input
    
# Execute the main function
if __name__ == "__main__":
    main()