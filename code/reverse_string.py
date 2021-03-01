# Python code to reverse a string
# using extended slice syntax

# Approach 1
str=input()
def reversestr(str):
    print(str[::-1])
reversestr(str)

# Approach 2
def reversestr2(str):
    string=""
    for char in str:
        string = char + string
    print(string)
reversestr2(str)

# Appproach 3

def reverse3(str):
    list=[None] * len(str)
    index= len(str) - 1
    for char in str:
        list[index] = char
        index -= 1
    return ''.join(list)
reversestr3(str)
