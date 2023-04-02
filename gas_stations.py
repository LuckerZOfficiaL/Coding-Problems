# -*- coding: utf-8 -*-
"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique

Idea: 
    create a list of balances, where each value is the difference between gas[i] and cost[i], which represents the gain or loss
    the indexes where the balance is <= 0 are certainly not possible starting points, others are candidates to the solution
    for each candidate index:
        check whether the balance gets negative, if not, the candidate index is the solution
    if no candidate index allowed the circuit completion, return -1 because it's impossible to complete the circuit
"""


def gas_stations(gas, cost):
    balance = []
    for i in range(0, len(gas)):
        balance.append(gas[i] - cost[i])
    candidates = [i for i in range(0, len(gas))] 
    for i in range(0, len(balance)):
        if balance[i] < 0:
            candidates.remove(i)      
    for c in candidates:
        if feasible_trip(gas, balance, c):
            return c
    return -1
        
def feasible_trip(gas, balance, i):
    current_balance = balance[i] 
    print("start station index: ", i)
    print("start balance = ", current_balance, "after exiting station ", i)
    
    for j in range(i+1, len(gas)):
        current_balance += balance[j]
        print("balance = ", current_balance, "after exiting station: ", j)
        if current_balance < 0:
            print("balance got negative!\n")
            return False
    for j in range(0, i):
        current_balance += balance[j]
        print("balance = ", current_balance, "after exiting station: ", j)
        if current_balance < 0:
            print("balance got negative!\n")
            return False
    print("Succesfully completed one circuit!\n")
    return True
        

print(gas_stations(gas = [2,3,4], cost = [3,4,3]))
print("---------------------------------------------------")
print(gas_stations(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    
    
