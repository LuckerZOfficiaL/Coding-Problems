# -*- coding: utf-8 -*-
"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251" is "23321511"
because we have 2 three's, 3 two's, 1 five, and one 1

"""

def count_and_say(n):
    output_seq = ""
    
    current_digit = n[0]
    current_count = 1
    
    i = 1
    while i < len(n):
        if n[i] != current_digit:
            output_seq = output_seq + str(current_count) + current_digit
            current_count = 0
            current_digit = n[i]
        else:
            i += 1
            current_count += 1
            
    output_seq = output_seq + str(current_count) + current_digit
    return output_seq


print(count_and_say("333332555"))
            
        
    
    

