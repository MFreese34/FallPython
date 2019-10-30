# -*- coding: utf-8 -*-
"""

Milo Freese
Python 2
Week 8 - Lambda Expression
October 30, 2019

"""

from functools import reduce

###############################################
# Single Argument Lambda assigned to variable #
###############################################
def single_lam():
    # assign variable to lambda expression
    y = lambda x: x + 5
    # print variable to console
    print('Single lamda expression: ', y(661))

############################
# Multiple Argument Lambda #
############################
def mul_lam():
    # establish variable to lambda expression
    shoe = lambda brand, shoe_type, color: f'Shoe: {brand.title()} | {shoe_type.title()} | {color.title()}'
    # assign values to variable from lambda expression var
    vans = shoe('Vans', 'Authentic', 'Red')
    # print variable
    print('Multiple lambda expression:', vans)

###############
# IIFE Lambda #
###############
def IIFE_lam():
    # Prompt user and obtain shoe price/quanitity
    shoe_price = int(input('Enter Shoe price: '))
    shoe_quant = int(input('Enter Quantity of Shoe: '))
    # Apply IIFE Lambda function - mutliply price by quanitity
    shoe_total = (lambda shoe_price, shoe_quant: shoe_price * shoe_quant)(shoe_price,
                 shoe_quant)
    # print total cost of shoe
    print('Total cost: ', shoe_total)
    
############################
# Lambda with map function #
############################
def map_lam():
    # Establish list
    shoe_quant = [65, 95, 115, 50, 175, 100, 75, 130]
    print('Original list:', shoe_quant)
    # Apply map function (division by 5) to each element within listA
    mod_shoe_q = list(map(lambda x: int(x / 5), shoe_quant))
    # Print modified list
    print('Modified list:', mod_shoe_q)
    
###############################
# Lambda with filter function #
###############################
def filter_lam():
    # Establish list
    shoe_price = [29.99, 34.99, 39.99, 54.99, 59.99, 69.99, 74.99]
    print('Original list:', shoe_price)
    # Apply filter function (greater than 15) to each element within list
    # New list is created with each item that results in true from filter
    mod_shoe_p = list(filter(lambda x: x > 40, shoe_price))
    # print modified list
    print('Modified list: ', mod_shoe_p)
    
###############################
# Lambda with reduce function #
###############################
def reduce_lam():	
    # Establish list
    shoe_price = [29.99, 34.99, 39.99, 54.99, 59.99, 69.99, 74.99]
    # apply rolling calculation to all items within list
    total_cost = reduce(lambda a, b: a + b, shoe_price)		
    # print result
    print('Total cost of shoes: ', total_cost)

############################
# Displays example options #
############################
def options():
    print('   Lambda Expression Examples')
    print('--------------------------------')
    print('1) Single Lambda Expression')
    print('2) Multiple Lambda Expression')
    print('3) IIFE Lambda Expression')
    print('4) Map Function')
    print('5) Filter Function')
    print('6) Reduce Function')
        
######################################
# Verify selection and call function #
######################################
def verify(num):
    while num > 0 and num <= 7:
        if num == 1:
            single_lam()
        elif num == 2:
            mul_lam()
        elif num == 3:
            IIFE_lam()
        elif num == 4:
            map_lam()
        elif num == 5:
            filter_lam()
        elif num == 6:
            reduce_lam()
            
        print()
        options()
        
        num = int(input('Enter another selection or enter [0] to end program: '))
        
#############################################
# Calls lambda expression example functions #
#############################################
def main():
    # display options
    options()
    # get option selection
    num = int(input('Enter Selection: '))
    # verify selection and call function
    verify(num)
    
# Execute the main function
if __name__ == "__main__":
    main()
