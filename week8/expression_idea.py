# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:52:26 2019

@author: Milo
"""

from functools import reduce

###########################
# Subtotal of shoe prices #
###########################
def subtotal():
# Establish list
    shoe_price = [29.99, 34.99, 39.99, 54.99, 59.99, 69.99, 74.99]
    # apply rolling calculation to all items within list
    sub = reduce(lambda a, b: a + b, shoe_price)		
   
    print('order subtotal:', sub)
        
    return sub
    
#######################################################
# Apply tax rate to subtotal and determine total cost #
#######################################################
def total_cost(sub):
    tax_rate = .07
    
    
    tax_total = (lambda tax, subtotal: tax * subtotal) (tax_rate, sub)
    
    print('tax total:', tax_total)
    
    total = sub + tax_total
    
    
    print('Order total:', total)

###################
# calls functions #
###################
def main():
    order_subtotal = subtotal()
    total_cost(order_subtotal)
    
# Execute the main function
if __name__ == "__main__":
    main()