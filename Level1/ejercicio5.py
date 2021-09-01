#read the file
obf = open("archivo.txt","r+")

# special arrays
words  = []
counts = []

# Read each line
for each in obf.readlines():
    # For each line separate words without new line special character
    for each_word in each.rstrip("\n").split(" "):
        # If next word doesn´t exist
        if each_word not in words:
            words.append(each_word)
            counts.append(1)
        # If next word exist
        else:
            index = words.index(each_word)
            counts[index] += 1

# Print each word an its repetitions
for a, each in enumerate(words):
    print (counts[a], " times the word: ", each)