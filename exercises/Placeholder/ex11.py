# Getting User Input in command line

print("How old are you?", end = ' ') # end = ' ' adds a space at the end
age = input() # get age user input
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = float(input()) # get user input, convert to float.

print(f"So, you're {age} years old, {height} tall, and weigh {weight}.")

target = float(input("How much would you like to weigh?\n"))

print(f"You need to gain {target-weight} lbs.")