#Jack Sweeney 7/17/18
#Program to draw "Jack's House" with functions for drawing the trees and houseName.
import turtle

#Draw a house
def drawHouse(houseName):
	#Main House
	houseName.color("blue")
	houseName.begin_fill()
	houseName.pensize(5)
	houseName.forward(60)
	houseName.left(90)
	houseName.forward(80)
	houseName.left(60)
	houseName.forward(35)
	houseName.left(60)
	houseName.forward(35)
	houseName.left(60)
	houseName.forward(80)
	houseName.left(90)
	houseName.forward(20)
	houseName.end_fill()
	#Door
	houseName.color("red")
	houseName.left(90)
	houseName.forward(25)
	houseName.right(90)
	houseName.forward(20)
	houseName.right(90)
	houseName.forward(25)
	
	

	

#Draw a tree
def drawTree(tree, x, y):
	#Trunk 
	tree.penup()
	tree.setpos(x, y)
	tree.pendown()
	tree.color("Brown")
	tree.pensize(5)
	tree.left(90)
	tree.forward(35)
	#Top
	tree.begin_fill()
	tree.color("green")
	tree.right(90)
	tree.circle(20)
	tree.end_fill()
	
def main():
	#Jacks House 
	jack = turtle.Turtle()
	jack.speed(10)
    drawHouse(jack)
	
	
	#Berry Tree 1
	berry1 = turtle.Turtle()
	drawTree(berry1, 100, 0) 
	
	#Berry Tree 2
	berry2 = turtle.Turtle()
	drawTree(berry2, -35, 0)

	#Artwork Name
	print "Jack's House(in low quality:L)"
	
    
main()