"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Idea: RECURSION
    at each step, fix one "pivot" value and seek permutations for the rest of the numbers
    each number in the array will, at certain point, be the "pivot" value.
"""

def permutations(nums):
    if len(nums) == 1:
        return [nums]
    output_permutations = []
    for i in range(0, len(nums)):
        next_permutations = permutations(nums[:i]+nums[i+1:])
        for perm in next_permutations:
            output_permutations.append([nums[i]] + perm)
    return output_permutations    


print(permutations([1,2,3,4]))