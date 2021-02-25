#Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.
numbers=[i for i in range(1,100)]
for index,num in enumerate(numbers):
    if num %3 == 0 and num % 5 == 0:
        numbers[index]='fizzbuzz'
    elif num % 3 == 0:
        numbers[index]='fizz'
    elif num % 5 == 0:
        numbers[index]='buzz'
    else:
        numbers[index]=num
print(numbers)