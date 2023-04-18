# -*- coding: utf-8 -*-
"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

For a visual example,check out the problem's webpage: https://leetcode.com/problems/max-area-of-island/
"""

def max_area(grid):
    indices = []
    for row in grid:
        this_row_indices = []
        for i in range(0, len(row)):
            if row[i] == 1:
                this_row_indices.append(i)
        indices.append(this_row_indices)
    segmented_indices = segmentation(indices)

    for row in segmented_indices:
        for segm in row:
            segm.append(len(segm))    
    max_area_updown = 0
    for i in range(1, len(segmented_indices)):
        for segm in segmented_indices[i]:
            for above_segm in segmented_indices[i-1]:
                if intersect(segm[:-1], above_segm[:-1]):
                    segm[-1] += above_segm[-1]
                if segm[-1] > max_area_updown:
                    max_area_updown = segm[-1] 
                    
    for row in segmented_indices:
        for segm in row:
            segm.append(len(segm)-1)
    max_area_downup = 0
    for i in range(len(segmented_indices)-2, -1, -1):
        for segm in segmented_indices[i]:
            for below_segm in segmented_indices[i-1]:
                if intersect(segm[:-2], below_segm[:-2]):
                    segm[-1] += below_segm[-1]
                if segm[-1] > max_area_downup:
                    max_area_downup = segm[-1]                  
    return max(max_area_downup, max_area_updown)
        
                       
    
def segmentation(indices):
    segmented_indices = []
    for row in indices:
        i = 0
        j = 0
        this_segment = []
        if len(row) == 1:
            this_segment.append(row)
        while j < len(row)-1:
            if row[j+1] != row[j]+1:
                this_segment.append(row[i:j+1])
                i = j+1
            j += 1
            if j == len(row)-1:
                this_segment.append(row[i:j+1])
        segmented_indices.append(this_segment)
    return segmented_indices
            
    
def intersect(list1, list2):
    return bool(set(list1) & set(list2))


print("\n",max_area([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                     [0,0,0,0,0,0,0,1,1,1,0,0,0],
                     [0,1,1,0,1,0,0,0,0,0,0,0,0],
                     [0,1,0,0,1,1,0,0,1,0,1,0,0],
                     [0,1,0,0,1,1,0,0,1,1,1,0,0],
                     [0,0,0,0,0,0,0,0,0,0,1,0,0],
                     [0,0,0,0,0,0,0,1,1,1,0,0,0],
                     [0,0,0,0,0,0,0,1,1,0,0,0,0]]))


