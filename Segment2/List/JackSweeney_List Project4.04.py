#Jack Sweeney 8/4/18
#This lets a user if they like similar cars to Jack and why. 

def main():
#Setting my top 5
    myFavCars = ["0", "Tesla Model X", "Lamborghini Aventador", "Audi R8", "BMW i8", "Chevrolet Corvette"]
	
	

#Asking user for top car
	userTopCar = input("Whats your favorite car?")
	
	if( userTopCar == "Tesla Model X" or userTopCar == "Model X" ):
		print "You like the Model X Too!, Electric is the way to go"
		
	elif( userTopCar == "Lamborghini Aventador" or userTopCar == "Aventador" ):
		print "You like speed too, might be fun but expensive."
		
	elif( userTopCar == "Audi R8" or userTopCar == "R8" ):
		print "Not a lambo fan too bad, I know R8s are still fast thats why their on my list."
		
	elif( userTopCar == "BMW i8" or userTopCar == "i8" ):
		print "I like the i8 too for the doors and its speed!."
		
	elif( userTopCar == "Chevrolet Corvette" or userTopCar == "Corvette" ):
		print "Atleast we both care for speed, but its american made. :("
	
	else:
		print "Too bad we don't like similar cars you must not care for speed"
	
#Printing My Top 5
	print "These are my top 5 cars!"
	for n in range(1, len(myFavCars)):
		print  str(n) + ". " + myFavCars[n]

main()