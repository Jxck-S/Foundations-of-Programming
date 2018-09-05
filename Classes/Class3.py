# Object-oriented Programming

class Contact:

    def __init__(self, name = "", phone = ""):
        # Create a new contact with name and phone.
        self.name = name
        self.phone = phone

def main():
 
    newContact = Contact("Monty", "123-555-9876")

    print("My Contacts")
    print("Name: " + newContact.name)
    print("Phone: " + newContact.phone)

main()