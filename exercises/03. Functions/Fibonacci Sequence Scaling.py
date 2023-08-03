# Scaling Fibonacci's Sequence

# Displays correct number of decimal places
# Displays correct number of leading zeros depending on the max number length

def fib_scale():
    # Get user input
    scale_factor = input("Input scaling factor: ")
    n_seq = int(input("Input length of sequence to scale: "))

    # Convert scale_factor to integer or float based on input.
    scale_factor = scale_factor.strip() # Remove extra spaces
    if scale_factor.endswith("%"):
        scale_factor = float(scale_factor[:-1])/ 100.0
    if "." in scale_factor:
        scale_factor = float(scale_factor)
    else:
        scale_factor = int(scale_factor)
    
    # Establish the sequence
    if n_seq <= 0:
        return []
    if n_seq == 1:
        return [0]
    if n_seq == 2:
        return [0, 1]
    # Start the sequence off
    fib_seq = [0, 1]
    # Start Loop to calculate new values of sequence
    for i in range(2, n_seq):
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)

    # Apply scaling factor to sequence
    scaled_seq = [n * scale_factor for n in fib_seq]

    # Ensure it will work with float and integers

    if isinstance(scale_factor, int):
        scale_format = "{:0" + str(len(str(max(scaled_seq)))) + "d}"
    else:
        scale_format = "{:0" + str(len(str(max(scaled_seq))) + 1) + ".2f}"

    print(f"{scale_format}") 

    print(f"""
    Scaling factor = {scale_factor}; Sequence length = {n_seq}\n
    Unscaled:   {", ".join(scale_format.format(num) for num in fib_seq)}
    Scaled:     {", ".join(scale_format.format(num) for num in scaled_seq)}
    """)
    
    return scaled_seq

fib_scale()