# -*- coding: utf-8 -*-
"""
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 

Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

For a visual illustration, go to the webpage: https://leetcode.com/problems/path-sum-ii/
"""

def path_sum_2(tree,targetSum):
    return recursive_path_sum(tree, 0, targetSum)




def recursive_path_sum(tree, i, targetSum):
    if is_leaf(tree, i) and tree[i] == targetSum:
        return [[targetSum]]  
    if targetSum <= 0:
        return [[]]  
    if tree[i] == None:
        return [[]]
    
    subseq_paths = []
    for child_index in [2*i + 1, 2*i + 2]: # for both children
        if child_index < len(tree) and tree[child_index] != None:
            child_paths = recursive_path_sum(tree, child_index, targetSum-tree[i])
            for child_path in child_paths:
                if child_path != []:
                    child_path.insert(0, tree[i])
                    subseq_paths.append(child_path)            
    return subseq_paths



def is_leaf(tree, i):
    if 2*i > len(tree): return True
    return False


print(path_sum_2([5,4,8,11,None,13,4,7,2,None,None,5,1,5],22))
        
    

    
    

