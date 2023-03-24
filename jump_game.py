# -*- coding: utf-8 -*-
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


"""
Let n be the length of the array
Use DYNAMIC PROGRAMMING:
    Let SOL be an boolean array where SOL[i] denote whether starting from num[i] I can get to the end
    
    -Base case: 
            SOL[n-1] = True 
    -General case: 
            SOL[i] = OR{ SOL[i+1],...,SOL[i+num[i]] }
    -Target:
        SOL[0]
"""

def jump_game(nums):
    n = len(nums)
    SOL = [0]*n
    SOL[n-1] = True
    for i in range(n-2, -1, -1): # the second argument is -1 because python range doesn't include the second extreme
        for j in range(i+1, i+nums[i]+1):
            if SOL[j] == True:
                SOL[i] = True
                break
        else:
            SOL[i] = False
    return SOL[0]


print(jump_game([2,3,1,1,4])) # true
print(jump_game([3,2,1,0,4])) # false
print(jump_game([1,1,1,1,1])) # true
print(jump_game([1,1,0,1,1])) # false  
print(jump_game([1,2,0,1,1])) # true  
    
