# Read a text file

from sys import argv

script, filename = argv

print(f"Opening {filename}.")
openFile = open(filename, 'r') # Read only
print(openFile.read())

openFile.close()
