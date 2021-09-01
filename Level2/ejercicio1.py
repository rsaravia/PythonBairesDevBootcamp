# 1. Write a Python program to scan a specified directory and identify the sub directories and files.
import os

#get all the elements of current working directory
l = os.listdir(os.getcwd())

print("elementos en ",os.getcwd(),": ", l)

for elemento in l:
    if os.path.isfile(os.path.join(os.getcwd(),elemento)):
        print(elemento, "is a file")
    else:
        print(elemento, "is a directory")




