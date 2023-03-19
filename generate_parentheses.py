# -*- coding: utf-8 -*-
"""
Given n, write a function to generate all combinations of n pairs of well-formed parentheses.

"""

def generate_parentheses(n): # interface function
    out_list= []
    generate(n, 0, 0, "", out_list)
    return out_list

# "current" contains the current string of parentheses
def generate(n, opened, closed, current, out_list):
    if opened == n and closed == n: # a string of parentheses is complete
        out_list.append(current)
    if closed < opened: # you can close only if closed < opened
        generate(n, opened, closed+1, current+")", out_list)
    if opened < n:
        generate(n, opened+1, closed, current+"(", out_list)
        

print(generate_parentheses(3))
        


    
    
    
    
    
        
    
