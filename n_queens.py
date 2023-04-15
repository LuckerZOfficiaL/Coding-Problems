# -*- coding: utf-8 -*-
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' respectively indicate a queen and an empty space.


Problem web page: https://leetcode.com/problems/n-queens/
"""

def no_attack_board(n):
    
    board = [n * "." for i in range(0, n)]
    output_boards = []
    recursive_boards(board, output_boards, n)
    return output_boards
    

def recursive_boards(current_board, output_boards, n):
    if n == 0:
        output_boards.append(current_board)
    
    for i in range(len(current_board)-n, len(current_board)): # it starts from the ith row because the previous rows all have a queen already
            for j in range(0, len(current_board[0][0])):
                if available(current_board, i, j):
                    new_row = ["."*(j-1) + "Q" + "." * (len(current_board[0][0])-j)]
                    recursive_boards(current_board[:i] + [new_row] + current_board[i+1:], output_boards, n-1)
                   
                   
def available(current_board, i, j):
    if "Q" in current_board[i][0]: # redundant? checking if a queen is in that row
        return False
    if exists_queen_on_column(current_board, j):
        return False
    if exists_queen_on_diagonal(current_board, i, j):
        return False
    if exists_queen_in_square(current_board, i, j):
        return False
    return True
    
    
    
def exists_queen_on_column(current_board, j):
    for row in current_board:
        if row[0][j] == "Q":
            return True
    return False
    
def exists_queen_on_diagonal(current_board, i, j):
    for r in range(0, len(current_board)):
        for c in range(0, len(current_board[0][0])):
            if abs(i-j) == abs(r-c) and current_board[r][0][c] == "Q":
                return True
            if abs(i+j) == abs(r+c) and current_board[r][0][c] == "Q":
                return True
    return False
    

def exists_queen_in_square(current_board, i, j):
    upmost = i-1
    bottommost = i+1
    leftmost = j-1
    rightmost = j+1
    
    if i == 0:
        upmost = 0
    if i == len(current_board)-1:
        bottommost = len(current_board)-1
    if j == 0:
        leftmost = 0
    if j == len(current_board[0][0])-1:
        rightmost = len(current_board[0][0])-1
    
    for r in range(upmost, bottommost+1):
        for c in range(leftmost, rightmost+1):
            if current_board[r][0][c] == "Q":
                return True
    return False

    
print(no_attack_board(4))

# There are some indexing problems to debug...
    
    

