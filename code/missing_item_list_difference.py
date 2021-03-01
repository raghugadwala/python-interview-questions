"""
Given an unsorted array of unique integers (size n + 1) and a second array that is identical to the first array but missing one integer (size n)
find and output the missing integer
"""
list1=[5,6,8,9]
list2=[8,5,9]

def missing_integer(list1,list2):
    dict2={x:0 for x in list2}
    for num in list1:
        if num not in dict2.keys():
              return num

number = missing_integer(list1,list2)
print(number)

# Approach2 using sum

def missing_integer_sum(list1, list2):
    return sum(list1) - sum(list2)
number = missing_integer_sum(list1,list2)
print(number)

# Apporch3 (removing from list)

def missing_integer_remove(list1, list2):
    for ele in list2:
        list1.remove(ele)
    return list1[0]
number = missing_integer_remove(list1,list2)
print(number)


