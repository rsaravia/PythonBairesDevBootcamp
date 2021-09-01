# 3. Write a Python program that accepts a filename from the user and prints the filename’s extension.
# Sample filename : abc.java
# Output : java

filename = input("Enter filename: ")
output = filename.rsplit(".",1)
print (output[-1])
