#Jack Sweeney 8/1/18
#This program lets a user draw somthing in turtle graphics with simple letter commands that chose which direction the turtle goes. 

import turtle
#Defining turtle Direction choices
def goForward(turtle):
	turtle.color("green")
	turtle.forward(60)

def goLeft(turtle):
	turtle.color("red")
	turtle.left(90)
	turtle.forward(60)

def goRight(turtle):
	turtle.color("blue")
    turtle.right(90)
	turtle.forward(60)

def main():
	pen = turtle.Turtle()
#Directions
	print "_____________________________________"
	print "Draw a picture by Using these letters"
	print "as direction choice for the turtle.     "
	print "__ Letter            Direction     __"
	print "__   R               Right         __"
	print "__   L               Left          __"
	print "__   F               Forward       __"
	print "_____________________________________"
#loop for repeating choice of direction 
	againStatus = "y"
	while(againStatus == "y"):

#Choosing direction
		direction = input ("Which way do you want to go ?  Use R, L and F for choice(right-R, left-L or forward-F) ")
	
		if( direction == "R" ):
			goRight(pen)
			againStatus = input("Would you like another move? (y/n) ")
		elif( direction == "L" ):
			goLeft(pen)
			againStatus = input("Would you like another move? (y/n) ")
		elif( direction == "F" ):
			goForward(pen)
			againStatus = input("Would you like another move? (y/n) ")
		else:
			print("Please enter a valid direction! (right-R, left-L or forward-F)")
			
    
    
main()