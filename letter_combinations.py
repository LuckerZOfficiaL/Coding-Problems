"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

The mapping of digits to lettersvis given below:
    2: abc
    3: def
    4: ghi
    5: jkl
    6: mno
    7: pqrs
    8: tuv
    9: wxyz
    
    
    
Idea: RECURSION
    where a problem is reduced into a smaller problem of one less digit.
"""


dictionary = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}


def letter_combinations(digits):
    output_strings = []
    if len(digits) == 1:
        for char in dictionary[digits[0]]:
            output_strings.append(char)
        return output_strings
    
    next_strings = letter_combinations(digits[1:])
    for char in dictionary[digits[0]]:
        for string in next_strings:
            output_strings.append(char+string)
                
    return output_strings    
   


print(letter_combinations([2,6,8]))