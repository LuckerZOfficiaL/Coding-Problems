# -*- coding: utf-8 -*-
"""
URL: https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
  
For example:   
    In the triangle:[[2],[3,4],[6,5,7],[4,1,8,3]]
    The minimum path cost is 11

        2
       3 4
      6 5 7
     4 1 8 3
     
     
Idea: DIVITE ET IMPERA
    each node defines a sub-triangle, and the minimum cost from a node in its sub-triangle 
    is the minimum between two costs, one following the left child, one following the right child.
    
    The base case is when the node is a leaf, it returns its own cost.
"""

def triangle_min_path(t):
    return recursive_path(t, 0, 0)

def recursive_path(triangle, depth, i):
    if i < 0 or i > len(triangle[depth])-1: # when index goes out of the range
        return float("inf")
    
    if depth == len(triangle)-1: # base case
        return triangle[depth][i]
    
    left_cost = recursive_path(triangle, depth+1, i)  # recursive call 1
    right_cost = recursive_path(triangle, depth+1, i+1) # recursive call 2
    return min(left_cost, right_cost) + triangle[depth][i] 


print(triangle_min_path([[1], [2,3],[4,5,6]]))
print(triangle_min_path([[2], [3,4],[6,5,7], [4,1,8,3]]))



