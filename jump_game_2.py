# -*- coding: utf-8 -*-
"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and
    i + j < n
    
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].

Idea: DYNAMIC PROGRAMMING
    create a vector M of size n where each entry stores the minimum number of jumps to reach nums[n-1]
    the vector is filled from right M[n-1] to left M[0], and the target value is M[0]
    
    Base case: M[n-1] = 0
    General case: M[i] = min{ M[i + 1],...,M[i + nums[i]]] } + 1

"""

def jump_game_2(nums):
    n = len(nums)
    M = [0]*n
    M[n-1] == 0
    for i in range(n-2, -1, -1):
        M[i] = min([M[i+j] for j in range(1, nums[i]+1) if i+j < n]) + 1
    return M[0]


print(jump_game_2([2,3,1,1,4]))
print(jump_game_2([1,1,1,1]))

