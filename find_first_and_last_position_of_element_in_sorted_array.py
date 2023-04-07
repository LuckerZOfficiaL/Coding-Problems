# -*- coding: utf-8 -*-
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Idea: Binary search twice
"""

def find_first_and_last(nums, elem):
    first_idx = bin_search(nums, elem, "first", 0, len(nums))
    last_idx = bin_search(nums, elem, "last", 0, len(nums))
    return [first_idx, last_idx]

def bin_search(nums, elem, command, i, j):
    med = int((j+i)/2)
    if command == "first":
        if nums[med] == elem and nums[med-1] < elem:
            return med
        if nums[med] >= elem:
            return bin_search(nums, elem, command, i, med)
        return bin_search(nums, elem, command, med, j)
    else: # command == "last"
        if nums[med] == elem and nums[med+1] > elem:
            return med
        if nums[med] <= elem:
            return bin_search(nums, elem, command, med, j)
        return bin_search(nums, elem, command, i, med)
        
    
print(find_first_and_last([1,2,2,2,3,3,3,4,5,5,5,6], 5))
        

        

