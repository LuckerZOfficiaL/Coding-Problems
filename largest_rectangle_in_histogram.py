# -*- coding: utf-8 -*-
"""
URL: https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

A visual example can be found in the Leetcode page linked above.

Idea: for each bar, check the area of the rectangle containing that bar. Keep the largest area and return it. 
"""

def largest_rectangle(h):
    current_largest = 0
    for bar_idx in range(0, len(h)-1):
        current_area = rectangle_area_from(h, bar_idx)
        if current_area > current_largest:
            current_largest = current_area
    return current_largest


def rectangle_area_from(h, bar_idx):
    partner_bars = 0
    
    i = bar_idx
    if i > 0:
        while h[i-1] >= h[bar_idx]: # count how many bars to the left are at least as high as h[bar_idx]
            partner_bars += 1
            if i-1 == 0: break
            else: i -= 1
     
    i = bar_idx
    if i < len(h)-1:
        while h[i+1] >= h[bar_idx]: # count how many bars to the right are at least as high as h[bar_idx]
            partner_bars += 1
            if i+1 == len(h)-1: break
            else: i += 1

    return (partner_bars + 1) * h[bar_idx]


print(largest_rectangle([2,1,5,6,2,3]))
print()
print(largest_rectangle([2,4]))
        
        




