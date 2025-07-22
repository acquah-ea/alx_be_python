#!/usr/bin/env python3

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Print the multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
