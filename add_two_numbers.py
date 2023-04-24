# -*- coding: utf-8 -*-
"""
You are given two non-empty lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

def add_two_numbers(num1, num2):
    num1.reverse()
    num2.reverse()
    Sum = []
    carry = 0
    for i in range(0, min(len(num1), len(num2))):
        if num1[i] + num2[i] + carry >= 10:
            Sum.append(num1[i] + num2[i] + carry - 10)            
            carry = 1
        else:
            if carry == 0:
                Sum.append(num1[i] + num2[i])
            else:
                carry = 0
                Sum.append(num1[i] + num2[i] + 1)
                    
    if len(num1) < len(num2):
        if carry == 1:
            for i in range(len(num1), len(num2)):
                if num2[i] + carry == 10:
                    carry = 1
                    Sum.append(0)
                else:
                    carry = 0
                    Sum.append(num2[i] + 1)
                    Sum += num2[i+1:]
                    break
            if carry == 1:
                Sum.append(1)
        else:
            Sum += num2[i:]
            
    elif len(num1) > len(num2): # this block of code is analogous to the previous block, I could have easily enclose them into one function
        if carry == 1:
            for i in range(len(num2), len(num1)):
                if num1[i] + carry == 10:
                    carry = 1
                    Sum.append(0)
                else:
                    carry = 0
                    Sum.append(num1[i] + 1)
                    Sum += num1[i+1:]
                    break
            if carry == 1:
                Sum.append(1)
        else:
            Sum += num1[i:]
            
    Sum.reverse()
    return Sum
     
                                               
            

print(add_two_numbers([2,2,3], [3,2,1]))
print(add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9]))