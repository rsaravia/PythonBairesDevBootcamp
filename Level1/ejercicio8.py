# Write a Python function to remove an item from a tuple.

# tuple define
tt = ('a','b','c','d','e')

# set elemento to remove (zero based index)
index = 1

tt = tt[:index]+tt[index+1:]

print (tt)