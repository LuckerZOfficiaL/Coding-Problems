# -*- coding: utf-8 -*-
"""
Given an integer array nums, 
return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.


Idea: 
    -sort the array in ascending order
    -start pointing at the rightmost number
        -for each number pointed:
            - for each number before it:
                check the two numbers' difference and sum
                if there can be a third edge, it must be within the range (dif, sum)
                so, count the number of entries between the two that are within this range and sum that to the counter
    -return the counter value
    
"""

def valid_triangle_number(nums):
    numbers = sorted(nums)
    count = 0
    for i in range(len(numbers)-1, 1, -1):
        for j in range(0, i):
            Dif = numbers[i] - numbers[j]
            Sum = numbers[i] + numbers[j]
            count += count_numbers_in_range(numbers[j+1:i], Dif, Sum)
    return count
            
    

def count_numbers_in_range(nums, left, right):
    count = 0
    for num in nums:
        if num <= right and num >= left:
            count += 1
    return count


print(valid_triangle_number([2,2,3,4]))


"""
Why it works?
 - This algorithm does not count any triangle more than once:
     because it starts from the right and it counts the numbers whithin the range only for array values between indexes i and j
     so, at every check, we fix the largest and the smallest edges of a hypothetical triangle and look for the remaining edge
     the remaining edge is only sought in the portion of the sorted array that is between the largest edge and the smallest
     
 - This algorithm doesn't leave out valid triangles:
     Suppose there is a triangle of edges (a,b,c) that the algorithm overlooked, where a < b < c.
     It must be the case that 
          a + b > c
          a + c > b
          b + c > a
    
    For sure, the algorithm at some iteration points at c with the outer for loop.
    For sure, the algorithm pointing at c will also point at a with the inner loop.
    Since a < b < c, b must lie between the indexes of a and c in the sorted array.
    The algorithm then counts the number of entries between indexes of a and c that have a value between dif = c-a and sum = a+c
    But b is guaranteed to be within that range of (dif, sum) because:
         b < sum because otherwise (a,b,c) cannot be a valid triangle
         b > dif because otherwise (a,b,c) cannot be a valid triangle
    
    Thus, the algorithm must have counted the triangle (a,b,c) during its execution.
     
"""
