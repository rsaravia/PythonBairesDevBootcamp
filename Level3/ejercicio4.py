# Write a Python function using list comprehension that receives a list of words and
# returns a list that contains:
# a. The number of characters in each word if the word has 3 or more characters
# b. The string “x” if the word has fewer than 3 characters

low = ['a','este','eso','aquello','tambien']

lor = [len(x) if len(x) >= 3 else 'x' for x in low]

print("Original list: ", low)
print("Output list: ", lor)