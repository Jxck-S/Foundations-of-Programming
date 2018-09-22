#Jack Sweeney 7/12/18
#This creates Joe a green and orange circular illusion 

import turtle

def main():

#Naming Turtle
    joe = turtle.Turtle()
    
#Making Joe 
    for joe in range(40):
	    joe.color("green")
        joe.forward(60)
        joe.left(105)
		joe.color("orange")
		joe.forward(60)
		joe.left(105)

	print "Joe"
    
main()