# Write a Python function to merge two dictionaries.

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5, 'f':6}

print ("dict1 (before): ", dict1)

for each in dict2:
    dict1[each] = dict2[each]


print ("dict1 (after): ", dict1)
