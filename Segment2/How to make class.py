Creating a Contact Class	
class Contact:	
Step 1: Define your class.

Use the Python keyword class to define a new class and give it a name. Here we are creating the class Contact.

class Contact: 

    def __init__(self):	
Step 2: Initialize.

Once you've defined a class, you'll use the_init_() method to initialize new objects. Every class needs one of these. When you create a new object, this method sets all of the initial values of that instance.

class Contact: 

    def __init__(self):
        self.name = ""
        self.phone = ""
Step 3: Set the parameter.

The parameter self plays a key role in a class. They are used to reference the object so it can set its attribute values. In this case, the attribute values are blank, as indicated by the empty quotation marks.

class Contact: 

    def __init__(self): 
        self.name = ""
        self.phone = ""
def main(): 
    newContact = Contact()
Step 4: Name your instance.

Once a class has been written, you can create instances of the object in your main method. Similar to creating an instance of a Turtle using a statement like t = Turtle(), the same can be done for a contact.

class Contact: 

    def __init__(self): 
        self.name = ""
        self.phone = ""

def main(): 
    newContact = Contact()
    print("Name:" + newContact.name + " " + newContact.phone)

main()
Step 5: Retrieve object values.

To retrieve the values for a contact object's name and phone number, use dot notation. To do this, write the name of the object, followed by a period (or dot), and then either an attribute or method. This lets Python know which instance of the object to use. Use dot notation when setting object values, as well.