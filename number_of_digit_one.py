# -*- coding: utf-8 -*-
"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

I will convert the integern n to string back and forth to easily get the digit at each index. Alternatively I can write a function to break down a number into int digits.

Idea: count the number of unit digits being 1, then the number of tens being 1, and so on 
"""

def number_of_digit_one(n):

    if n == 0:
        return 0
    if n < 10:
        return 1

    strn = str(n)
    count = 0
    
    for i in range(len(strn), 1, -1):   
        if strn[i-1] == "0": 
            count = count + ((len(strn)-i+1) * int(strn[:i-1]))
        else:
            count = count + ((len(strn)-i+1) * (int(strn[:i-1]) + 1))
            
    # special case for the last and most significant digit
    count = count + int(strn[1:]) + 1
    return count
    
    
print(number_of_digit_one(12))
print(number_of_digit_one(13))
print(number_of_digit_one(123))


    


    
        
