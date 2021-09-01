# Write a Python program that takes an input string from the user and counts the frequency of characters in the string.
# Sample String : google.com
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

s = input("Enter a sting (any size): ")

# initialize variables
characters = []
count = []

for each_char in s:
    if each_char not in characters:
        characters.append(each_char)
        count.append(1)
    else:
        index = characters.index(each_char)
        count[index] += 1

dictionary = dict(zip(characters, count))
print (dictionary)