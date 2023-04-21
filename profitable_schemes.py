# -*- coding: utf-8 -*-
"""
There is a group of n members, and a list of various crimes they could commit. 
The ith crime generates a profit[i] and requires group[i] members to participate in it. 
If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, 
and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. 


Example: 
    Input: n = 5, minProfit = 3, groups = [2,2], profit = [2,3]
    Output: 2
    Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
                    In total, there are 2 schemes.
                    
                    
IDEA: Recursion and then remove duplicate schemes
"""

def profitable_schemes(n, minProfit, group, profit):
    schemes = []
    indexed_group = []
    for i in range(0, len(group)):
        indexed_group.append([i, group[i]])
    recursive_schemes(n, minProfit, indexed_group, profit, [], schemes)
    return len(list(set(frozenset(scheme) for scheme in schemes)))
    

# current_scheme is a list of indices, where an index j represents group j being deployed
def recursive_schemes(n, minProfit, group, profit, current_scheme, schemes):
    #print("-----, current scheme:", current_scheme)

    if minProfit <= 0:
        schemes.append(set(current_scheme))
    
    for i in range(0, len(group)):
        if group[i][1] <= n: # if we have enough members for group[i]
            my_scheme = current_scheme.copy()
            my_scheme.append(group[i][0])
            recursive_schemes(n - group[i][1], 
                               minProfit - profit[group[i][0]], 
                               group[:i] + group[i+1:], 
                               profit,
                               my_scheme,
                               schemes)




print(profitable_schemes(5, 3, [2,2], [2,3]))
print(profitable_schemes(10, 5, [2,3,5], [6,7,8]))
        
    
    

