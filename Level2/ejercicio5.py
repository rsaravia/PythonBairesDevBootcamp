# 5. Create a Python function that accepts any number of positional and keyword arguments,
# and that prints them back to the user.
# Your output should indicate which values were provided as positional arguments,
# and which were provided as keyword arguments.


def print_function(*positional, **keywords):
    for i in positional:
        print("Positional argument: ",i)
    for key,value in keywords.items():
        print("Keyword argument ",key," : ",value)

print_function(1,2,3,a=1,b=2,c=3)

print(" ")

print_function('a','b','c','d','e','f',uno=1,dos=2,tres=3,cuatro=4)
