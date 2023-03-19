# -*- coding: utf-8 -*-
"""
You are given an n x n 2D matrix, rotate the maty 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

def rotate_matrix(matrix):
    if len(matrix) > 1:     
        rotate_external(matrix)
        
        smaller_matrix = [] # I just need to get inner matrix elements by reference, I dunno how to do it, so the code doesn't really work
        for i in range(1, len(matrix)-1):
            smaller_matrix.append(matrix[i][1:-1])
        print("\nsmaller matrix: ", smaller_matrix)
        rotate_matrix(smaller_matrix)
    



def rotate_external(matrix):
 
    if len(matrix) == 2: # base case
        matrix[0][0], matrix[1][0] = matrix[1][0], matrix[0][0]
        matrix[0][0], matrix[1][1] = matrix[1][1], matrix[0][0]
        matrix[0][0], matrix[1][0] = matrix[1][0], matrix[0][0]

    n = len(matrix)
    
    uprow = []
    rightcol = []
    downrow = []
    leftcol = []
    
    for i in range(0, n):
        uprow.append(matrix[0][i])
    
    for i in range(n-1, -1, -1):
        rightcol.append(matrix[i][n-1]) 
        
    for i in range(0, n):
        downrow.append(matrix[n-1][i]) 
    
    for i in range(n-1, -1, -1):
        leftcol.append(matrix[i][0]) 
        
    print("uprow: ", uprow)
    print("rightcol: ", rightcol)
    print("downrow: ", downrow)
    print("leftcol: ", leftcol)
        
    
    for i in range(0, n): 
        matrix[0][i] = leftcol[i] # topmost row = left column
        matrix[i][n-1] = uprow[i] # rightmost column = topmost row
        matrix[n-1][i] = rightcol[i] # bottomost row = right column
        matrix[i][0] = downrow[i] # left column row = bottomost row
        
        
matrix = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]    
rotate_matrix(matrix)
print(matrix)
        
        

    
    
        
    
    
    
    

