# -*- coding: utf-8 -*-
"""
Week 2 Looping Exercises

"""

def main():
    Ex1() 
    Ex2()

def Ex1():
    # Iterate value to 100
    for i in range(102): 
        # Determine if value is divisible by 2
        if (i % 2) == 0: 
            # Print even number value
            print(i, end =" ")  
    print()
def Ex2():
    # Declare string
    string = 'KABOOM'
    
    # declare count letters
    K = 3
    A = 3
    B = 3
    O = 6
    M = 3
    
    # iterate variable through string
    for x in range(len(string)):
        # determine if letter is in string value of variable  
        if 'K' in string[x]:
            # Loop until count variable is zero
            while K > 0:
                # print letter
                print('K', end = " ")
                # decrement variable
                K -= 1
        elif 'A' in string[x]:
            while A > 0:
                print('A', end = " ")
                A -= 1
        elif 'B' in string[x]:
            while B > 0:
                print('B', end = " ")
                B -= 1
        elif 'O' in string[x]:
            while O > 0:
                print('O', end = " ")
                O -= 1
        elif 'M' in string[x]:
            while M > 0:
                print('M', end = " ")
                M -= 1
        
    
def Ex3():
    # Declare string
    string = "askaliceitthinksshe'llknow"

            
# Execute the main function
if __name__ == "__main__":
    main()