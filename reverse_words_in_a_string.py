# -*- coding: utf-8 -*-
"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

def reverse_string_words(s):
    words = break_down(s)
    words.reverse()
    output = ""
    for word in words:
        output = output + word + " "
        
    return output
        
def break_down(s):
    word_list = []
    i = 0
    while True:
        current_word = ""
        while s[i] == " ":
            i += 1
        if i == len(s)-1:
            break
            
        while s[i] != " ":
            current_word += s[i]
            if i < len(s)-1:
                i += 1
            else:
                break    
        word_list.append(current_word)
        
        if i == len(s)-1:
            break     
    return word_list

print(reverse_string_words("  hi everyone     this is Leetcode"))
        
        
        

     
    
        