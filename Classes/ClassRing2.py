# Object-oriented Programming

class Contact:

    def __init__(self, name = "", phone = "", ringtone = ""):
        # Create a new contact with name and phone.
        self.name = name
        self.phone = phone
        self.ringtone = ringtone

    def playRingtone(self):
        # Play ringtone assigned to the Contact
        if(self.ringtone == "Hello"):
            print("Hello, it's me")
        elif(self.ringtone == "Shake It Off"):
            print ("Cause the players gonna play, play, play, play, play")  
        elif(self.ringtone == "Single Ladies"):
            print("Cause if you liked, then you shoulda put a ring on it")
        else:
            print("Ring, ring")


def main():

    newContact = Contact("Monty", "123-555-9876", "Hello")

    print("Name: " + newContact.name)
    print("Phone: " + newContact.phone)
    print("Ringtone: " + newContact.ringtone)


    newContact.playRingtone()                # Play Monty's ringtone
    newContact.ringtone = "Shake It Off"     # Change Monty's ringtone

    print("")
    print("Name: " + newContact.name)
    print("Phone: " + newContact.phone)
    print("New Ringtone: " + newContact.ringtone)
    newContact.playRingtone()                # Play ringtone again

main()