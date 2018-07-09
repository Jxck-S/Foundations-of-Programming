#Jack Sweeney 6/24/18
#Math word problem- Calculates the volume and surface area of a cube 

def main():
    print ("Jimmy has a box to put his gifts in and he wants to know how much volume he has for the items.  He also wants to know the surface area of the box to wrap the box, His box is a cube.")
	edge = float(input("Whats the length of one of the sides on Jimmy's Box?"))
	#Calculations
	volume = pow(edge, 3)
	sa = (pow(edge, 2)) * 6
	print ("The volume of Jimmy's Box is ") + str(volume)
	print ("The surface area of the outside of Jimmy's Box is ") + str(sa)
	
main()