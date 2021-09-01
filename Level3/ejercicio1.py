# Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are the same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

l = ['abc','xyz','aba','1221']

#l = ['aba','aa','abba','bcccc','vvvvv']

counter = 0

for each in l:
    if len(each) >= 2 and each[0]==each[-1]:
        counter += 1

print("Result: ", counter)