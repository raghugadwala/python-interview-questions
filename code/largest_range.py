# Given an unsorted array of integers nums, return the the longest consecutive elements range.
# sample input [1,5,9,8,4,10]
# output [8 10] #[8,9,10]

list = [int(num) for num in input().split()]
dict = {x:0 for x in list}
left = right = 0

for number in list:
    if dict[number] == 0:
        count_left=number-1
        count_right=number+1

        while count_left in dict:
            dict[count_left]=1
            count_left -= 1
        count_left += 1
        while count_right in dict:
            dict[count_right] = 1
            count_right += 1
        count_right -= 1
        if (right-left) <= (count_right-count_left):
            left=count_left
            right=count_right
print(left,right)
