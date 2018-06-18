#Jack Sweeney 6/16/18 
#This program asks basic information about a person and responds  back with the information 

#Program
def main():
    firstName = input ("Whats your first name?")
	print ("Hello there ") + firstName 
	gender = input ("Whats your gender?")
	print ("I'm glad to see your ") + gender + (", Im  ") + gender + (" too")
	age = input ("How old are you?")
	print ("Wow your ") + age + (" too, we have alot in common!")
	lastName = input ("Whats your last name?")
	fullName = firstName + (" ") + lastName 
	print  ("Your last name starts with an ") + (lastName[0]) + ("; Mine does too!")
	print  ("The first two letters in your first name are ") + firstName[0:2]
	print  ("Nice to meet you ") + fullName + (" seeya later!")
	

main()