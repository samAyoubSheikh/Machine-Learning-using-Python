# react with yes , if random number generated is prime

import random as rd


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = rd.randint(0,200)

if num < 2:
    print("No..")
else:
    prime = True

    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Yes :",num)
    else:
        print("No.. :",num)


#react with yes if there are three consecutive prime numbers generated

count = 0
for i in range(10):
    x = rd.randint(0,20)
    print(x, end=" ")

    if is_prime(x):
        count+=1
    else:
        count=0
    if count == 3:
        print("Yes, three consecutive prime numbers generated")
        break
