# -*- coding: utf-8 -*-
"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
    - Insert a character
    - Delete a character
    - Replace a character
    
IDEA: use Levenshtein Distance
"""

def edit_distance(word1, word2):
    if word1 == word2: 
        return 0
    if len(word1) == 0:
        return len(word2) # because len(word2) characters must be inserted
    if len(word2) == 0:
        return len(word1) # because len(word1) characters must be inserted
    if word1[0] == word2[0]:
        return edit_distance(word1[1:], word2[1:])
    
    return 1 + min(edit_distance(word1[1:], word2), # equivalent to removing the first char of word1
                    edit_distance(word1, word2[1:]), # equivalent to removing the first char of word2
                    edit_distance(word1[1:], word2[1:])) # equivalent to replacing the first char of word1 with that of word 2


print(edit_distance("horse", "ros"))
    


