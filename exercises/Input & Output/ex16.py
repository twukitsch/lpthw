from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

prompt_OpenArgs = """Choose from the following list:
      a = append (add to end of file)
      w = completely overwrite the file with new text
      x = create a new file and open it for writing"""

OpenArgs = ['a', 'w', 'x']

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
    else:
        print("\nERROR. You must chose one of the values from the list.\nIt should be a single letter\n\a")


# Trucate basically deletes the contents of the file when it has no argument.
# It can also be used to resize the file to a certain number of bytes with the 'size' argument
# Is this necessary though? Since the 'w' argument in open() above truncates the file first?
# target.truncate()
# Yes, truncate is redundant and unneccesary. If 'w' argument wasn't present in the open() function it would have worked.

print("Now Im going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# Saves the file stored in the "target" object.
target.close()

