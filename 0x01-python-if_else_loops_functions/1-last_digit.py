#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    buf = number * -1
else:
    buf = number

last_digit = buf % 10
if number < 0:
    last_digit = last_digit * -1

if last_digit == 0:
    print(f"Last digit of {number:d} is 0 and is 0")

elif last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")

elif last_digit < 6:
    print(f"Last digit of {number:d} is {last_digit:d}\
 and is less than 6 and not 0")
