# 4. Write a Python program to count the number of lines in a text file.

# Open a file
fo = open("ejercicio5.py", "r+")
print ("Name of the file: ", fo.name)

lines = fo.readlines()
print ("Number of lines: %i" % (len(lines)))

# Close opened file
fo.close()