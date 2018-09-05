# Object-oriented Programming

class Contact:

    def __init__(self, name = "", phone = "", ringtone = "", duesOwed = 0):
        # Create a new contact with name and phone.
        self.name = name
        self.phone = phone
        self.ringtone = ringtone
        self.duesOwed = duesOwed

    def payDues(self, money):
        # Compute the dues owed for the club membership.
        self.duesOwed = self.duesOwed - money

def main():

    newContact = Contact("Monty", "123-555-9876", "Hello", 12.50)

    print("Name: " + newContact.name)
    print("Phone: " + newContact.phone)

    print("Dues owed: $" + str(newContact.duesOwed))
    payment = 10.00
    newContact.payDues(payment)
    print("Dues owed now: $" + str(newContact.duesOwed))

main()