# Lists in Python

def main():

    names = ["Chewy", "Captain Kirk", "Hermione", "Storm", "Buzz"]

    length = len(names)

    print("The original list: ")
    print(names)
    print("")

    # Replace a value in the list
    names[1] = "Spock"
    print("Spock replaces Captain Kirk: ")
    print(names)
    print("")

    # Append a value to the end of the list
    names.append("Rex")
    print("Rex is added to the list: ")
    print(names)
    print("")
    
    # Delete a value from the list
    del names[4]
    print("Buzz is deleted from the list: ")
    print(names)

main()