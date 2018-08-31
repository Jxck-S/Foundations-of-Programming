# Number Systems

def main():

    # User input
    b = "0b" + input("Enter a binary number: ")

    print("Your binary number is: " + b)

    # Convert a binary number to a decimal
    # int(the number, the base)
    d = int(b, 2)
    print("The decimal equivalent is: " + str(d))

main()