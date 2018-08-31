# Number Systems

def main():

    # Assign a decimal number to d
    d = 7

    # Convert d to a binary number
    b = bin(d) 
    print("The binary value is: " + b)

    # Convert a binary number to a decimal
    # int(the number, the base)
    d = int(b, 2)
    print("The decimal value is: " + str(d))

main()