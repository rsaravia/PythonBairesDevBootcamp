# Write a Python program that reads a JSON object from a file,
# sorts the object keys in ascending order,
# then writes the JSON object back into the file.
import json

"""
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    },
    "coworker": {
        "name": "Roberto Saravia",
        "species": "pythonist"
    }

}
"""

# Open file to read
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print("Original File: ","\n",data)


# Open file to write
with open("data_file2.json", "w") as write_file:
    json.dump(data, write_file,sort_keys=True)
