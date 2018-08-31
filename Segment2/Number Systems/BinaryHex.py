# Number Systems

def main():

    # Print Table Headings
    print("     Number Systems Chart     ")
    print("Decimal   Binary   Hexadecimal")
    # Print body of table
    for d in range (0, 16):
        b = bin(d)
        h = hex(d)
        print("   " + str(d) + "       " + b + "        " + h)

main()