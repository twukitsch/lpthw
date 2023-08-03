# The interface is just begging to be turned into a function here
# (!f Potential Function)

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

prompt_OpenArgs = """Choose from the following list:
      a = append (add to end of file)
      w = completely overwrite the file with new text
      x = create a new file and open it for writing
      r = open in read only format
      add a '+' after the letter to open in read & write mode"""

OpenArgs = ['a', 'w', 'x', 'r', 'r+', 'a+', 'w+', "x+"]

exitLoop = False
while exitLoop != True:
    print(prompt_OpenArgs)
    out_OpenArgs = input(">> ")

    if out_OpenArgs in OpenArgs:
        if out_OpenArgs == 'a':
            print("Opening the file to append...")
            target = open(filename, out_OpenArgs)
            exitLoop = True

        if out_OpenArgs == 'w':
            print("Opening the file and overwriting...")
            target = open(filename, out_OpenArgs)
            exitLoop = True

        if out_OpenArgs == 'x':
            print("Creating and opening a new file...")
            target = open(filename, out_OpenArgs)
            exitLoop = True

        if out_OpenArgs == 'r':
            print("Opening file in read-only mode...")
            target = open(filename, out_OpenArgs)
            exitLoop = True

        if out_OpenArgs == 'a+':
            print("Opening the file to append & read...")
            target = open(filename, out_OpenArgs)
            exitLoop = True

        if out_OpenArgs == 'w+':
            print("Opening the file and overwriting; read enabled...")
            target = open(filename, out_OpenArgs)
            exitLoop = True

        if out_OpenArgs == 'x+':
            print("Creating and opening a new file with read enabled...")
            target = open(filename, out_OpenArgs)
            exitLoop = True

        if out_OpenArgs == 'r+':
            print("Opening file with read and write enabled...")
            target = open(filename, out_OpenArgs)
            exitLoop = True
    else:
        print("\nERROR. You must chose one of the values from the list.\nIt should be a single letter\n\a")


# Trucate basically deletes the contents of the file when it has no argument.
# It can also be used to resize the file to a certain number of bytes with the 'size' argument
# Is this necessary though? Since the 'w' argument in open() above truncates the file first?
# target.truncate()
# Yes, truncate is redundant and unneccesary. If 'w' argument wasn't present in the open() function it would have worked.

print("Please input three lines of text.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Writing these to the file.\n\n")

target.write(f"{line1}\n{line2}\n{line3}\n")

# Read the file
print("File Contents:\n")
target = open(filename, 'r')
print(target.read())

print("And finally, we close it.")
# Saves the file stored in the "target" object.
target.close()

