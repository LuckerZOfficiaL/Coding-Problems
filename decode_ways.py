# -*- coding: utf-8 -*-
"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the 
reverse of the mapping above (there may be multiple ways). 

For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is INVALID because "06" cannot be mapped into 'F' since "6" is different from "06".


Given a string s containing only digits, return the number of ways to decode it.
"""

vocab = {"A":"1", "B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"10","K":"11"
         ,"L":"12","M":"13","N":"14","O":"15","P":"16","Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22"
         ,"W":"23","X":"24","Y":"25","Z":"26"}

def decode_ways(message):
    if len(message) == 0: return 1
    count = 0
    for char in vocab.keys():
        if message.startswith(vocab[char]):
            count += decode_ways(message[len(vocab[char]):])
    return count


print(decode_ways("11106"))
print(decode_ways("12"))
print(decode_ways("226"))
print(decode_ways("06"))