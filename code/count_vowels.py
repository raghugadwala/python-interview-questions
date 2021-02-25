# Python program to check
# count number of vowels in string

vowels=['a','e','i','o','u']
str=input()
str=str.lower()
def vowelscount(str):
    count=0
    for char in str:
        if char in vowels:
            count+=1
    print(count)
vowelscount(str)