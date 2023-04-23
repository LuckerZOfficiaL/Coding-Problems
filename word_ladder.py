# -*- coding: utf-8 -*-
"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. 
    Note that beginWord does not need to be in wordList.
    sk == endWord
    
Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


IDEA: recursion
"""


def word_ladder(beginWord, endWord, wordList):
    result = recursive_word_ladder(beginWord, endWord, wordList, 1)
    if result == float("inf"):
        return 0
    return result



def recursive_word_ladder(beginWord, endWord, wordList, currLen):   
    if beginWord == endWord:
        return currLen
    else:
        next_lens = []
        for i in range(0, len(wordList)):
            if diff_by_one(beginWord, wordList[i]):
                Next = recursive_word_ladder(wordList[i], endWord, wordList[:i]+wordList[i+1:], currLen+1)
                next_lens.append(Next)
        if len(next_lens) > 0: 
            return min(next_lens)
        return float("inf")
    
    

def diff_by_one(str1, str2):
    if len(str1) != len(str2):
        return False
    diff_count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
        if diff_count > 1:
            return False
    return True



print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]))

        
