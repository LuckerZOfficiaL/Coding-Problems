# -*- coding: utf-8 -*-
"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 

If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Idea: 
    removing useless border characters doesn't change the outcome
    iteratively cut s from left or right:
        compare the shortest string of s from left contianing all characters in t againast from right
        if left range is smaller, remove from s the rightmost character in t and then remove the useless border if there is any
        if right range is smaller, shrink s from the left
    the loop ends when the remaining s cannot be further shrunk
    
    
Note: this implementation ignored the request that duplicates in t must also be included in the window.
    
"""

def minimum_window_substring(s, t):       
    freqs = [] # array of frequencies of characters in t
    for char in t:
        freqs.append(t.count(char))
    s = remove_borders(s, t)
    while keep_going(s, t, freqs): 
        left_range = calculate_range(s, t, "left", freqs)
        right_range = calculate_range(s, t, "right", freqs)
        if left_range <= right_range:
            s = s[:-1]
        else:
            s = s[1:]
        s = remove_borders(s, t)
    return s
    
    
                    
def remove_borders(s, t): # removes the useless characters at both sides
    left_start_index = 0
    right_remove_index = len(s)-1
    while s[left_start_index] not in t:
        left_start_index += 1
    while s[right_remove_index] not in t:
        right_remove_index -= 1
    return s[left_start_index:right_remove_index+1]


def calculate_range(s, t, direction, freqs): # calculates the length of the left or right-starting substring of s that contains all characters in t
    if direction == "left":
        i = 1
        while not all_appear_at_least(s[:i], t, freqs):
            i += 1
        return i
    else:
        i = len(s)-1
        while not all_appear_at_least(s[i:], t, freqs):
            i -= 1
        return len(s)-i
        

def keep_going(s, t, freqs): # the loop should keep going if by removing any border character, the characters of t are still present in s with at least their frequencies
    if not all_appear_at_least(s, t, freqs):
        return False
    if all_appear_at_least(s[:-1], t, freqs) or all_appear_at_least(s[1:], t, freqs):
        return True
    

def all_appear_at_least(s, t, freqs): # true if s contains all characters of t with at least the frequency indicated in freqs
    for i in range(0, len(t)):
        if s.count(t[i]) < freqs[i]:
            return False
    return True




print(minimum_window_substring("ADOBECODEBANC", "ABC"))
print(minimum_window_substring("ADDSCSAWRRSC", "ASSW"))


