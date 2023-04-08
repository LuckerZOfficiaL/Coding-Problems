# -*- coding: utf-8 -*-
"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word 
is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Idea: RECURSION
    Scan through s from the left, for each string that appears in WordDict, save that word in words_found.
    For each word found x, recursive call the function on the portion of s starting after the word x.
"""

def word_break(s, wordDict):
    sentences = []
    recursive_word_break(s, wordDict, "", sentences)
    return sentences
    
def recursive_word_break(s, wordDict, current_sentence, sentences):
    if s in wordDict:
        sentences.append(current_sentence + " " + s)
        
    words_found = []
    i = 1
    while i < len(s)-1:
        if s[0:i] in wordDict:
            words_found.append(s[0:i])
        i += 1
    for word_found in words_found:
        recursive_word_break(s[len(word_found):], wordDict, current_sentence + " " + word_found, sentences)
        
print(word_break("pineapplepenapple",["apple","pen","applepen","pine","pineapple"]))
print()
print(word_break("catsanddog",["cat","cats","and","sand","dog"]))
        
    
    
    
    
