# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:58:12 2019

@author: Milo
"""

from Mogwai import mog_discog

#########################################
# Main Function calls example functions #
#########################################
def main():
    # module example
    print('Mogwai Discography')
    print('------------------')
    module()
    
    print('\nList Comprehension Example #2')
    print('-----------------------------')
    l_comp()
    
##################
# Module Example #
##################
def module():
    # declare variable to list from module
    alb = mog_discog()
    
    # iterate through list
    for item in alb:
        print(item)

##############################
# List Comprehension example #
##############################
def l_comp():
    # declare list
    countdown = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
    
    # iterate through list and perform function
    countdown = [x - 10 for x in countdown]
    
    # print list
    print(countdown)
    
if __name__== '__main__':
    main()