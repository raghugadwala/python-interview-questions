# Python program to check if
# given number is prime or not

number=int(input())
def prime(number):
    if number > 1:
        num= number//2 + 1
        for i in range(2,num):
            if number%i == 0:
                print(number,"is not prime number")
                break
        else:
            print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')
prime(number)
