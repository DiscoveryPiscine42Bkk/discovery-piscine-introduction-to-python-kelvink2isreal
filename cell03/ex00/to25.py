#!/usr/bin/env python3
num = int(input("Enter a number less than 25\n"))
if num > 25:
    print("Error")
if num < 25 or num == 25:
    i = num
    while i <= 25:
        print(f"Inside the loop, myy variable is {i}")
        i += 1

