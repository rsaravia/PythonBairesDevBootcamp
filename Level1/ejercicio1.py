# 1. Write a Python program to test whether a passed letter is a vowel or not.
import openpyxl

vowel_list = ['A','a','E','e','I','i','O','o','U','u']

letter = input("Enter a letter: ")
if letter in vowel_list:
    print(letter, "is a Vowel")
else:
    print(letter, "is not a Vowel")
