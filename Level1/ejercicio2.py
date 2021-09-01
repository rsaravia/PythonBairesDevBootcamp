# 2. Write a Python program that accepts the user's
# first and last name and prints them in reverse order with a space between them.

first = input("Enter first name (then Enter): ")
last  = input("Enter last name (then Enter): ")

print(last[::-1],first[::-1])