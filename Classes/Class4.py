# Object-oriented Programming

class Contact:

    def __init__(self, name = "", phone = ""):
        # Create a new contact with name and phone.
        self.name = name
        self.phone = phone

def main():

    newContact = Contact("Monty", "123-555-9876")
    newContact2 = Contact("Dan", "321-555-9905")

    print("My Contacts")
    print("Name         Phone")
    print( newContact.name + "      " +  newContact.phone)
    print( newContact2.name + "        " +  newContact2.phone)  

    # Update Dan's phone number
    newContact2.phone = "543-555-9876"

    print("")
    print("My Updated Contacts")
    print("Name         Phone")
    print( newContact.name + "      " +  newContact.phone)
    print( newContact2.name + "        " +  newContact2.phone)   

main()