#4. Create a Python function that accepts any number of numbers as positional
# arguments and prints the sum of those numbers.

def sum_var(**variable):
    out = 0
    for key,value in variable.items():
        #print(key,value)
        out += value
    return out

print(sum_var(a=1, b=2, c=3))

print(sum_var(a=1,b=2, c=3, d=4, e=10))

