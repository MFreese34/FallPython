# -*- coding: utf-8 -*-
"""
Milo Freese
DAT129 - Python 2
Week 3
String Formatting Exercise

"""

def main():
    # present names in list
    name_list()
    print()
    # present names in greeting
    greeting()
    
# Presents names in a list organized by first and last names
def name_list():
    
    # Open file
    with open('names.txt', mode='r') as names:
        # print header
        print(f'{"First Name |":<10}{"Last Name":>10}')
        print('----------------------')
        
        for record in names:
            # split the name into two different values
            first_name, last_name = record.split()
            # display names
            print(f'{first_name:<10}{last_name:>12}')
   
# Displays names in a greeting form
def greeting():
    
    # Open file
    with open('names.txt', mode='r') as names:
        
        for record in names:
            # split names into two different values
            first_name, last_name = record.split()
            # display greeting with integrated name values
            print(f'Good evening Dr. {last_name}, would you mind if I called',
                  f'you {first_name}?')
   
# Execute the main function
if __name__ == "__main__":
    main()    