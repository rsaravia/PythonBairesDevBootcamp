# Project - Simple Calculator
# The objective is to write an interactive calculator. User input is assumed to be
# a formula that consists of a number, an operator (at least + and -), and
# another number, separated by white space (e.g. 1 + 1).
# Split user input and check whether the resulting list is valid:
# 1. If the input does not consist of 3 elements, raise a FormulaError,
#    which is a custom Exception.
# 2.Convert the first and third input to a float. Handle any ValueError that occurs,
#   and instead raise a FormulaError.
# 3. If the second input is not '+' or '-',
# again raise a FormulaError.
#
# If the input is valid, perform the calculation and print out the result.
# The user is then prompted to provide new input, and so on, until the user enters quit.
#
# An interaction could look like this:
#
# >>> 1 + 1
# 2.0
# >>> 3.2 - 1.5
# 1.7000000000000002
# >>> quit


class FormulaError(Exception):
    print("error")


# While is not 'quit'
while True:

    # input variable
    i = input("Provide an input or ´quit´ to go: ")

    if i != 'quit':
        # evaluated that has 3 elements
        # -----------------------------
        try:
            a,b,c = i.split()
        except ValueError:
            raise FormulaError("3 Elements are require")
        else:
            try:
                a = float(a)
                c = float(c)
            except ValueError:
                raise FormulaError("Can not convert to float..!!")
            else:
                if b == "+":
                    result = a + c
                    print(result)
                elif b == "-":
                    result = a - c
                    print(result)
                else:
                    raise FormulaError("Sign not available.!!")
        #-----------------------------
    else:
        print("Bye..!!")
        break
