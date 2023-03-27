# -*- coding: utf-8 -*-
"""
Given an m x n matrix, return all elements of the matrix in spiral order
"""
import math

def spiral_matrix(mat):
    num_rounds = min(math.ceil(len(mat)/2), math.ceil(len(mat[0])/2))
    read_nums = []
    print("Rounds: ",num_rounds)
    if num_rounds == 0:
        return read_external(mat, 0)
    for i in range (0, num_rounds):
        read_nums.extend(read_external(mat, i))
    return read_nums

def read_external(mat, round_num):
    read_nums = []
    print("\nFixed Row:",round_num)
    print("read right: Cols", round_num,len(mat[0])-round_num)
    for i in range(round_num, len(mat[0])-round_num): # read to right
        read_nums.append(mat[round_num][i])
        
    print("\nFixed Col:",len(mat[0])-round_num-1)
    print("read down: Row", round_num+1,len(mat)-round_num)
    for i in range(round_num+1, len(mat)-round_num): # read down
        read_nums.append(mat[i][len(mat[0])-round_num-1])
        
    print("\nFixed row:",len(mat)-round_num-1)
    print("read left: Cols", len(mat[0])-2-round_num,round_num-1)
    for i in range(len(mat[0])-2-round_num, round_num-1, -1): #read to left
        read_nums.append(mat[len(mat)-round_num-1][i])
        
    print("\nFixed col:",round_num)
    print("read up:", len(mat)-2,round_num)    
    for i in range(len(mat)-2 ,round_num, -1): # read up
        read_nums.append(mat[i][round_num])
    return read_nums

print(spiral_matrix([[0,1,2],[3,4,5],[6,7,8]]))
print()
print(spiral_matrix([[0,1],[2,3],[4,5],[6,7]]))
        

        

        
        
         
    
    

