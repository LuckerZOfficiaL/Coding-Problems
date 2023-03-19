# -*- coding: utf-8 -*-
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""



def two_sum(in_nums, target):
    print("target: ", target)
    if target == 0:
        print("target==0")
        return []
    
        
    for num in in_nums:
        nums = [n for n in in_nums] # copy the input numbers
        print("num: ", num)
        if num <= target:
            
            nums.remove(num)
            print("nums: ", nums)
            result = two_sum(nums, target - num)
            print("------result: ", result)
            if type(result) == list:
                print("type of results: ", type(result))
                result.append(num)
                print("returned: ", result)
                return result
  
         
print("\n\n Output: ",two_sum([2,3,4,6], 8))

    



    