# Write a Python program that iterates through integers from 1 to 100 and prints them.
# For integers that are multiples of three, print "Fizz" instead of the number.
# For integers that are multiples of five, print "Buzz".
# For integers which are multiples of both three and five print, "FizzBuzz".

l = [x+1 for x in range(100)]

for each in l:
    if ( each%3 == 0 ) and ( each%5 == 0 ):
        print ("FizzBuzz")
    elif (each%3 == 0):
        print ("Fizz")
    elif (each%5 == 0):
        print ("Buzz")
    else:
        print(each)
