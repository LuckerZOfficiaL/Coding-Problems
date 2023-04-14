# -*- coding: utf-8 -*-
"""
There are n children standing in a line. 
Each child is assigned a rating value given in the integer array "ratings".

You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    
Return the minimum number of candies you need to have to distribute the candies to the children.

For example:
    Input: ratings = [1,2,2]
    Output: 4
    
    Explanation: 
        You can allocate 1, 2, 1 candies respectively.
        The third child gets 1 candy because every one gets at least 1 and his/her rating is not higher than his heighbor's.
"""

def min_candies(ratings):
    candy_count = 0
    segments = monotonous_segments(ratings)
    for segment in segments:
        candy_count += (len(segment)-1) * (len(segment)) / 2 # the formula of the first n natural numbers
    
    for i in range(0, len(segments)-1):
        if segments[i][0] == "decreasing" and segments[i+1][0] == "increasing":
            candy_count = candy_count + len(segments[i+1]) - 1
    return int(candy_count)
        
    


def monotonous_segments(ratings):
    segments = []
    i = 0
    while True:
        cur_segment = []
        
        if i == len(ratings) - 1:
            cur_segment.append("equal")
            cur_segment.append(ratings[i])
            segments.append(cur_segment)
            return segments
    
        if ratings[i] < ratings[i+1]:
            cur_segment.append("increasing")
            cur_segment.append(ratings[i])
            while ratings[i] < ratings[i+1]:
                cur_segment.append(ratings[i+1])
                i += 1
                if i > len(ratings) - 2:
                    segments.append(cur_segment)
                    return segments   
            
        elif ratings[i] > ratings[i+1]:
            cur_segment.append("decreasing")
            cur_segment.append(ratings[i])
            while ratings[i] > ratings[i+1]:
                cur_segment.append(ratings[i+1])
                i += 1
                if i > len(ratings) - 2:
                    segments.append(cur_segment)
                    return segments
                        
        else:
            cur_segment.append("equal")
            cur_segment.append(ratings[i])
            
        segments.append(cur_segment)
        
        i +=1        
            
    
print(min_candies([1,2,2]))

                
        
    
    
        