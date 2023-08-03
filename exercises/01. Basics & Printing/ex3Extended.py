numbers = [109.9234785, (17/3), 12.35439]

for x in numbers:
    print("{:10.4f}".format(x)) # The empty string before the colon means "take the next provided argument to format()""
    # In this case, the x is the only argument
    # 10 is for 10 spaces filled to the left to center the numbers around the decimal point
    # 4 indicates the number of decimal points

fibonacci = [0, 1, 1]
i = 2
x = fibonacci[2]

print("{:7.1f}".format(0.0))
print("{:7.1f}".format(1.0))
print("{:7.1f}".format(1.0))

while x < 100:
    fibonacci.append(x + fibonacci[i-1]) # Appends the resulting number onto the end of the fibonacci vector
    i = i + 1
    x = fibonacci[i]
    print("{:7.1f}".format(x)) # The empty string before the colon means "take the next provided argument to format()""
    # In this case, the x is the only argument

print(fibonacci)
