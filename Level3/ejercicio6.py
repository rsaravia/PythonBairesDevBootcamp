# Write a python file with two functions: a function that receives a number
# and appends to a global variable list, and another function that returns
# this list ordered.
global_list = [8, 6, 1]

def receives_f(number):
    global_list.append(number)

def returns_f():
    global_list.sort()
    return global_list

while True:
    num = input("Enter a number or 'quit' to go: ")
    if num == "quit":
        print("Bye..!")
        break
    else:
        receives_f(int(num))
        #print(global_list)
        print(f"Number {num} was added!")
        print("Sorted List: ", returns_f())