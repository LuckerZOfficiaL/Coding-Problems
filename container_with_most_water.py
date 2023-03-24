# -*- coding: utf-8 -*-
"""
Problem LINK: https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the MAXIMUM AMOUNT OF WATER a container can store and the container borders.


Idea: 
    Start from the extremeties with two pointers on the endpoints of the container. 
    The pointer that has to move to the center one step is the one pointing at the minimum border height.
    This is because moving the other endpoint to the center would certainly not increase the container capacit as the minimum border height is unchanged.

    This has runningtime O(n) where n = len(heights)
"""

def container_with_most_water(heights):
    current_max = 0
    best_left_endpoint = None
    best_right_endpoint = None
    
    left_ptr = 0
    right_ptr = len(heights)-1
    
    while(left_ptr < right_ptr):
        current_volume = (right_ptr - left_ptr) * min(heights[left_ptr], heights[right_ptr])
        if current_volume > current_max:
            current_max = current_volume
            best_left_endpoint = left_ptr
            best_right_endpoint = right_ptr
            
        if heights[left_ptr] < heights[right_ptr]: # if the height of the left endpoint is smaller, the left pointer moves one step to the center
            left_ptr += 1
        else:
            right_ptr -= 1
            
    return [current_max, best_left_endpoint, best_right_endpoint]


print(container_with_most_water([1,8,6,2,5,4,8,3,7])) # should be [49, 1, 8]

