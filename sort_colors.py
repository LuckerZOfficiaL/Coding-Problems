# -*- coding: utf-8 -*-
"""
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


IDEA: scan the array from the left, push "0" elements to the left of the array and push "2" elements to the right
"""

def sort_colors(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums = push_left(nums, i)
        if nums[i] == 2:
            nums = push_right(nums, i)
        i += 1
    return nums
             
    
def push_right(nums, i):
    nums = nums[:i] + nums[i+1:] + [nums[i]]
    return nums
    
def push_left(nums, i):
    nums = [nums[i]] + nums[:i] + nums[i+1:]
    return nums
    

print(sort_colors([2,0,2,1,1,0]))
print(sort_colors([2,0,1]))
    
    

