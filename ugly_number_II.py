# -*- coding: utf-8 -*-
"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.


IDEA: Dynamic Programming    
"""

def nth_ugly_number(n):
    ugly_nums = [1]*n
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    
    for i in range(0, n):
        Next = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        ugly_nums[i] = Next
        
        if Next == next_multiple_of_2:
            next_multiple_of_2 = ugly_nums[i2] * 2
            i2 += 1
        if Next == next_multiple_of_3:   
            next_multiple_of_3 = ugly_nums[i3] * 3
            i3 += 1
        if Next == next_multiple_of_5:
            
            next_multiple_of_5 = ugly_nums[i5] * 5
            i5 += 1     
    return ugly_nums[-1]


print(nth_ugly_number(9))
print(nth_ugly_number(10))
    
    
    
    



