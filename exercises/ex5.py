name = 'TJ Wukitsch'
age = 33 # Not a lie
height = 5*12+8 # inches
weight = 170 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall (or {height*2.54} centimeters).")
print(f"He's {weight} lbs heavy (or { round( weight * 0.4535924, 2) } kgs).")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")
