# -*- coding: utf-8 -*-
"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Idea: 
    - the number of steps the robot has to take by only walking down or right is (m-1)+(n-1) = m+n-2
    - the correct output of the algorithm is really just be the number of permutations of m+n-2 steps, having m-1 steps down and n-1 steps right
    - there is the mathematical formula for this: (m+n-2)!/[(m-1)! (n-1)!]

"""

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output
        

def unique_paths(m, n):
    return int(factorial(m+n-2)/(factorial(m-1) * factorial(n-1)))

print(unique_paths(3, 2))
print()
print(unique_paths(3, 7))