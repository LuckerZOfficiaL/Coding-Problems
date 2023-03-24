# -*- coding: utf-8 -*-
"""
Given an array of integer intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Assume that starti <= starti+1. (if you don't have this assumption, you can just sort the list firts by starti)

For instance:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    
    
    
Idea:  imagine always having a "current interval", the one we are focusing on
   -start with the first interval being the "current interval"
   -check whether some intervals have started not after the end of the "current interval" but after the start of "current interval"
        -if yes, for the first such interval
            -check whether it is still open 
                -if yes: "current interval" = this interval, and go on
                -if no: there will be no "current interval" for now
                    -get to the next-starting interval and that is our new "current interval"
    repeat
    
    
    during the process, memorize the gaps where there is no "current interval"
    then the output of the algorithm is the whole interval [start0, endn] with gaps cut away
                
"""

def merge_intervals(intervals):
    gaps = []
    current_interval_index = 0
    have_been_current_indexes = []
    
    while(current_interval_index != None):
        go_forward = True
        for i in range(0, len(intervals)):
            if ((intervals[i][0] >= intervals[current_interval_index][0]) 
            and (intervals[i][0] <= intervals[current_interval_index][1])
            and (i not in have_been_current_indexes)): # if it started before the end of the current
                current_interval_index = i
                have_been_current_indexes.append(i)
                go_forward = False
                break
            
        if go_forward == True:
            if current_interval_index + 1 < len(intervals):
                gaps.append([intervals[current_interval_index][1], intervals[current_interval_index+1][0]])
                current_interval_index += 1
                have_been_current_indexes.append(current_interval_index)
            else:
                current_interval_index = None

    
    
    whole_interval = [intervals[0][0], max(intervals, key=lambda x:x[1])[1]]
    output = []
    previous_start = whole_interval[0]
    for gap in gaps:
        output.append([previous_start, gap[0]])
        previous_start = gap[1]
    output.append([previous_start, whole_interval[1]])
    return output
        
    
    

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
        
        
    
    