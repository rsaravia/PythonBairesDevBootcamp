#Write a Python function to remove duplicates from a list.

lista = [1,1,2,2,3,4,5,6,7,7,8,1,7,8]

"""
# initialize a repeated objets
not_duplicated_list = []

for each in lista:
    if each not in not_duplicated_list:
        not_duplicated_list.append(each)
"""

s = set(lista)
lista_out = [x for x in s]


print ("original list: ",lista)
print ("list with elements duplicates removed: ", lista_out)

