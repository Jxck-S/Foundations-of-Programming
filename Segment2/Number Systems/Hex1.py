# Number Systems

def main():

    # Assign a decimal number to d
    d = 156
    print("The decimal value is: " + str(d))

    # Convert d to a binary number
    h = hex(d) 
    print("The hexadecimal value is: " + h)

    # Convert a binary number to a decimal
    # int(the number, the base)
    d = int(h, 16)
    print("The decimal value again: " + str(d))

main()