# -*- coding: utf-8 -*-
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

def recursive_median(arr1, arr2):
    if len(arr1) == 2 and len(arr2) == 3:
        return sorted([min(arr1[1], arr2[2]), arr2[1], max(arr1[0], arr2[0])])[1]
    if len(arr1) == 3 and len(arr2) == 2:
        return sorted([min(arr1[2], arr2[1]), arr1[1], max(arr1[0], arr2[0])])[1]
    med1 = arr1[int(len(arr1)/2)]
    med2 = arr2[int(len(arr2)/2)]
    
    if med1 > med2:
        return recursive_median(arr1[:1+int(len(arr1)/2)], arr2[int(len(arr2)/2):])
    else:
        return recursive_median(arr1[int(len(arr1)/2):], arr2[:1+int(len(arr2)/2)])
    



