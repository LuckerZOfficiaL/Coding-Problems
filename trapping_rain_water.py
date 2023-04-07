# -*- coding: utf-8 -*-
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

There is a graphic illustration on the website of Leetcode: https://leetcode.com/problems/trapping-rain-water/

Idea: 
    first calculate the intervals (indexes of left and right column) that contain water
    for each interval, calculate how much water is trapped
    sum up all the waters
"""


def calculate_trapped_water(h):
    water_intervals = []
    i = 0
    while i < len(h):
        current_interval = find_next_water_interval(h, i)
        water_intervals.append(current_interval)
        i = current_interval[1]
    water_intervals.pop()

    water = 0
    for water_interval in water_intervals:
        water += calculate_interval_water(h, water_interval)
    return water
        

def find_next_water_interval(h, i):
    j = i
    if j+1 < len(h):
        while h[j] <= h[j+1] or max(h[j+1:]) < h[j]:
            j += 1
            if j >= len(h)-1:
                break
    start_idx = j
    
    j += 1
    if j >= len(h)-1:
        return [len(h), len(h)]
    
    while h[j] < h[start_idx]:
        j += 1
        if j >= len(h)-1:
            break
    
    if j > len(h)-1:
        return [len(h), len(h)]  
    return [start_idx, j]

def calculate_interval_water(h, water_interval):
    min_column_height = min(h[water_interval[0]], h[water_interval[1]])
    
    water_accumulated = 0
    for i in range(water_interval[0]+1, water_interval[1]):
        water_accumulated = water_accumulated + min_column_height - h[i]
    return water_accumulated
        
    
    
print(calculate_trapped_water([4,2,0,3,2,5]))
print()
print(calculate_trapped_water([0,1,0,2,1,0,1,3,2,1,2,1]))

        
        
        
        
