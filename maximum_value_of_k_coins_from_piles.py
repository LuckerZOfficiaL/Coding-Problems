# -*- coding: utf-8 -*-
"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, 
and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.


A graphical illustration can be found on the problem's page: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/


IDEA: 
    at each of the k steps, choose max{ piles[i][0] + maximum_value(piles[i][1:], other piles intact...)} for each i < n
"""


def maximum_value(piles, k):
    if k == 0: 
        return 0
    
    to_pop = []
    for i in range(0, len(piles)):
        if len(piles[i]) == 0:
            to_pop.append(i)
    for i in to_pop:
        piles.pop(i)
        
    max_value = 0
    for value in [(piles[i][0]+maximum_value(piles[:i]+[piles[i][1:]]+piles[i+1:], k-1)) for i in range(0, len(piles))]:
        if value > max_value:
            max_value = value    

    return max_value


print(maximum_value([[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7))
print(maximum_value([[1,100,3],[7,8,9]], 2))
        