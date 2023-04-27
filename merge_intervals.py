# -*- coding: utf-8 -*-
"""
Given an array of integer intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.


For instance:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    
    

IDEA: use a Stack
        sort the intervals by start time
        use a stack as the output list
        start with the stack containing the first interval
        iteratively check the intervals in ascending order of start time
        for each subsequent interval:
            if non-overlapped with the stack-top interval:
                add it to the stack
            else (there is overlap):
                update the stack-top interval's end time with the maximum between its original and the end time of the new interval
        return the stack
    
TIME OPTIMIZATION: calculate the maximum end time among all intervals, we can break the loop as soon as any end time is at least this value.


COMPLEXITY: 
        O(nlog(n)) running time for sorting, where n = #intervals
        O(n) spatial complexity to store the stack
"""


def merge_intervals(intervals):
        intervals.sort(key = lambda x: x[0])
        Max = max(intervals, key = lambda x: x[1])[1] # the maximum end value of an interval

        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if stack[-1][1] < intervals[i][0]: # non-overlapping with the current stack-top interval
                stack.append(intervals[i])
            else:
                stack[-1][1] = max(intervals[i][1], stack[-1][1])
            if stack[-1][1] >= Max: break # I can break the loop early if the right extreme is at least Max
        return stack
        
    
    

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
        
        
    
    