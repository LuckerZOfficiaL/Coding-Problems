# -*- coding: utf-8 -*-
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.



IDEA: Dictionary (Hashmap)
    for each number in the input, check whether there's another number in the hashmap that sums up to target with the current number
        if there is one, return the two indices
        if there is not, add the current number and index to the hashmap
        
    the motivation behind using a Hashmap is for its constant access time, which makes the whole algorithm run in linear time.
"""



def two_sum(nums, target):
    num_index_hashmap = {} # contains: key=value, value=index
    for index, num in enumerate(nums):
        try:
            index2 = num_index_hashmap[target-num]
        except KeyError:
            num_index_hashmap.setdefault(num, index)
        else:
            return sorted([index, index2])
            
         
print("\n\n Output: ",two_sum([17,2,3,4,6,7], 24))

    



    