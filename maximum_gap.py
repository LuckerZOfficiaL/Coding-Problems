# -*- coding: utf-8 -*-
"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

IDEA: 
    create an auxiliary array of counters with len(nums) entries, index i counts the frequency of value Min+i in nums
    scan through nums and increase the relative counters in num_counts
    the length of the largest consecutive subarray of zeroes in num_counts + 1 is the answer
    
This algorithm has runtime: O(n+range) and auxiliary memory: O(range)
"""


def max_gap(nums):
    if len(nums) < 2:
        return 0
    Max = max(nums)
    Min = min(nums)
    num_counts = [0 for num in range(Min, Max+1)]
    
    for num in nums:
        num_counts[num-Min] += 1
    
    max_gap = 0
    current_gap = 0
    i = 0
    while i < len(num_counts):
        if num_counts[i] != 0:
            current_gap = 0
        else:
            current_gap += 1
            if current_gap > max_gap:
                max_gap = current_gap
        i += 1
    return max_gap+1
            

print(max_gap([3,6,9,1]))
print(max_gap([24,5,2,20,9,22,1])) # sorted array would be [1,2,5,9,20,22,24]
    
    
    