# -*- coding: utf-8 -*-
"""
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. 
Apply the following algorithm on arr:
    -Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
    -Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
    -Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer n, return the last number that remains in arr.
"""

def elimination_game(n):
    numbers = list(range(1, n+1))
    turn = "left"
    while(len(numbers) > 1):
        print("\nCurrent Numbers: ",numbers)
        next_numbers = []
        if turn == "left":
            for i in range(1, len(numbers), 2): #starts from 1 because the 0th element doesn't survive
                next_numbers.append(numbers[i])
            numbers = next_numbers
            print("turn: ", turn)
            print("Resulting Numbers: ", numbers)
            turn = "right"
        elif turn == "right":
            for i in range(len(numbers)-2, -1, -2): 
                next_numbers.append(numbers[i])
            numbers = next_numbers
            numbers.reverse()
            print("turn: ", turn)
            print("Resulting Numbers: ", numbers)
            turn = "left"
            
    return numbers


print(elimination_game(9))
    

