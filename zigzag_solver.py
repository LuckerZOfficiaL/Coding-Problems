def zigzag_solver(string, k):
    n = len(string)
    green_indexes = []
    green_indexes.append(k-1)
    current_count = k-1
    while(current_count + 2*(k-1) < n):
        green_indexes.append(current_count + 2*(k-1))
        current_count = current_count + 2*(k-1)
        
    added_indexes = []
    solution = []
    for i in range(k-1, -1, -1):
        for green_index in green_indexes:
            if (green_index - i) >= 0:
                if (green_index - i) not in added_indexes:
                    added_indexes.append(green_index - i)
                    solution.append(string[green_index - i])
            if (green_index + i) < n:
                if (green_index + i) not in added_indexes:
                    added_indexes.append(green_index + i)
                    solution.append(string[green_index + i])
    return solution
    
    
print(zigzag_solver("PAYPALISHIRING", 3))