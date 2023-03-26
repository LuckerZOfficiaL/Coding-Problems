"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or use Python casting directly.

Example:
    Input: num1: "2", num2: "3"
    Output: "6"
"""

get_digit ={
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9    
}

get_string = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9"    
}

def multiply_strings(n1, n2):
    int1 = make_integer(n1)
    int2 = make_integer(n2)
    int_product = int1 * int2
    string_product = make_string(int_product)
    return string_product

def make_integer(strnum): # if I pass "123", I get 123
    int_n = 0
    for i in range(len(strnum)-1, -1, -1):
        int_n += get_digit[strnum[i]] * (10**(len(strnum)-1-i))
    return int_n
    

def make_string(intnum): # if I pass 123, I get "123"
    num_list = get_digit_list(intnum) 
    strnum = ""
    for intdigit in num_list:
        strnum += get_string[intdigit]
    return strnum

def get_digit_list(intnum): # if I pass 123, I get [1,2,3]
    num_list = []
    while intnum > 0:
        temp = 0
        while intnum%10 != 0:
            intnum -= 1
            temp += 1
        num_list.append(temp)
        intnum = intnum / 10
    num_list.reverse()
    return num_list      


print(multiply_strings("3", "11"))

