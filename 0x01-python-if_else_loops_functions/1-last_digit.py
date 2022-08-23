#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = int(number)
num = number
d = 1000
if num < 0:
    neg_num = num
    num *= -1
else:
    neg_num = num
for i in range(3):
    num %= d
    d /= 10
num = int(num)
if neg_num < 0:
    num *= -1
    if num > 5:
        print(f"Last digit of {number:d} is {num:d} and is greater than 5")
    elif num == 0:
        print(f"Last digit of {number:d} is {num:d} and is 0")
    elif num < 6 and not 0:
        print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
else:
    if num > 5:
        print(f"Last digit of {number:d} is {num:d} and is greater than 5")
    elif num == 0:
        print(f"Last digit of {number:d} is {num:d} and is 0")
    elif num < 6 and not 0:
        print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
