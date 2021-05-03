# Python Program for n-th Fibonacci number
number=int(input())
def fibonacci(n):
    if n < 0:
        print("Enter Positive number")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        num1=0
        num2=1
        for i in range(1,number):
            next_number=num1+num2
            num1=num2
            num2=next_number
        return (next_number)
print(fibonacci(number))