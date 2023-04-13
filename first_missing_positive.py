# -*- coding: utf-8 -*-
"""
Given an unsorted integer array nums, return the smallest missing positive integer.

for example, if L = [3,4,5], the first positive missing is 1. Positive numebers start from 1. 

You must implement an algorithm that runs in O(n) time and uses constant extra space.

IDEA:
    first remove all elements that are <= 0 
    suppose there are n positive elements left, we can exploit indices to check the presence of numbers:
    for each element num in nums: mark the num-th element in nums
    traverse the array starting from index 1, the first INDEX with an unmarked number is the FIRST MISSING POSITIVE.
    
    
    The problem becomes how to mark an element but such that it is still usable for traversing the list.
    An element in the array is marked if its value is >= the first multiple of N above the max. 
    This is because to ensure that unmarked values have a value < max.
    
    To still be able to traverse the array with augmented values, 
        for each value num, I use it to locate the index at position (num-first_multiple_above_max)%first_multiple_above_max
        This position index would be the same either when it is the original value num and when its value is increased by first_multiple_above_max

"""

def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        if nums[i] <= 0:
            nums.pop(i)
        else:
            i += 1
            
    N = len(nums)
    max_val = max(nums) # the maximum number in the array
    first_multiple_above_max = max_val # the first multiple of N above max_val
    for i in range(0, N):
        if (max_val + i) % N == 0:
            first_multiple_above_max = max_val + i

    for num in nums:
        if num < N or num >= first_multiple_above_max: 
            nums[-1 + (num-first_multiple_above_max) % first_multiple_above_max] += first_multiple_above_max
        
    for i in range (0, len(nums)):
        if nums[i] <= max_val:
            return i+1
    return N+1


print(first_missing_positive([7, -2, 0, 5, 1, 3, 2, 8]))
print(first_missing_positive([3,4,-1,1]))         
    
    
            
    
    
    
    
    
            
    
