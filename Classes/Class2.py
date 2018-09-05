# Object-oriented Programming

class Contact:

    def __init__(self):
        # Create a new contact with name and phone.
        self.name = ""
        self.phone = ""

def main():

    newContact = Contact()
    print("Initial value of name: " + newContact.name)

    # Give the Contact a name
    newContact.name = "Monty"
    print("Updated value of name: " + newContact.name)

main()