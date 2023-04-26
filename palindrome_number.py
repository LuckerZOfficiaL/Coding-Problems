# -*- coding: utf-8 -*-
"""
Given an integer x, return true if x is a  palindrome, and false otherwise.

E.g. 121 is palindrome.
"""

def isPalindrome(n):
    num = n
    digit_list = []
    while(True):
        digit = 0
        while num % 10 != 0:
            num -= 1
            digit += 1
        digit_list.append(digit)
        num = num/10
        if num == 0:
            break
        
    for i in range(0, int(len(digit_list)/2)):
        if digit_list[i] != digit_list[len(digit_list)-1-i]:
            return False
    return True
        
        
print(isPalindrome(122))
print(isPalindrome(121))