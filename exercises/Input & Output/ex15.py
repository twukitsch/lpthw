# Import argv to assign variables from command line
from sys import argv

# Lists variables, in order, to be named in command line
script, filename = argv

# Open the file and return it (store it) to an object called 'txt'
txt = open(filename)

print(f"Here's your file {filename}:")
# Prints ex15_sample.txt's text (in the txt object) out using the read() function
print(txt.read())


print("Type the filename again:")
# Uses user input during run to get the filename instead of argv prior to run
file_again = input("> ")

# Opens the file again allowing the object returned to be interacted with using
# file-oriented functions like read() or write()
txt_again = open(file_again)
# Uses the read function on txt_again without any additional arguments (uses defaults)
print(txt_again.read())

txt.close()
txt_again.close()
