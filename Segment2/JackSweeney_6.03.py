#Jack Sweeney 9/22/18
#my program is to ask a user about the information they know about the SpaceX BFR. If the user knows everything it will give them some facts and a turtle graphic.

import turtle

def main():

	userGuessBFR = ""
	userGuessBFR = input("Elon Musk and his company SpaceX want to go to Mars with their planned BFR what do you think BFR stands for?")
	if( userGuessBFR == "Big Falcon Rocket" or userGuessBFR == "big falcon rocket" ):
		print ("Your right! BFR stands for Big Falcon Rocket")
		winAmount = 1
	else:
		print ("BFR actually stands for Big Falcon Rocket")
		winAmount = 0 
		
		
	userGuessMonths = 0
	userGuessMonths = int(input("How long do you think it will take to travel to Mars with Elon Musks new BFR(Months)?"))
	if( userGuessMonths == 3 or userGuessMonths == 2 ):
		print ("Elon also thinks it may take 3 to 2 months to get to Mars with his new BFR. He'd like to make it one month.")
		winAmount = winAmount + 1
	elif( userGuessMonths > 3 ):
		print ("Elon thinks that its gonna take less than four months to get to Mars with his new BFR but you think othewise. (Next time put lower than 4)")
		winAmount = winAmount + 0
	elif( userGuessMonths == 1 ):
		print ("Wow you must really believe in Elon Musk and his company, he'd like to believe it'l take one month but he thinks like 2 to 3 months")
		winAmount = winAmount + 1
	if( winAmount >= 2):
		spaceRockets = ["Falcon 1", "Falcon 5", "Falcon Heavy", "BFR"]
		spaceRockets = ["", "Falcon 1", "Falcon 5", "Falcon Heavy", "BFR"]
		rockets = len(spaceRockets) - 1
		print ("Somthing you may not know SpaceX has " +  str(rockets) + " rockets in their rocket family.")
		for n in range(1, len(spaceRockets)):
			print(str(n) + ". " + spaceRockets[n] + "!")
		rocket = turtle.Turtle()
		rocket.hideturtle()
		rocket.speed(10)
		rocket.pensize(4)
		rocket.left(90)
		rocket.color("black")
		rocket.begin_fill()
		rocket.forward(100)
		rocket.left(45)
		rocket.forward(35)
		rocket.left(90)
		rocket.forward(35)
		rocket.left(45)
		rocket.forward(100)
		rocket.left(90)
		rocket.forward(50)
		rocket.end_fill()
		rocket.penup()
		rocket.left(90)
		rocket.forward(80)
		rocket.left(90)
		rocket.forward(10)
		rocket.pendown()
		rocket.pensize(4)
		rocket.color("grey")
		rocket.begin_fill()
		rocket.fillcolor("blue")
		rocket.forward(30)
		rocket.left(90)
		rocket.forward(18)
		rocket.left(90)
		rocket.forward(30)
		rocket.left(90)
		rocket.forward(18)
		rocket.end_fill()
		rocket.penup()
		rocket.left(180)
		rocket.forward(18)
		rocket.right(90)
		rocket.forward(30)
		rocket.left(90)
		rocket.forward(20)
		rocket.color("white")
		rocket.write("SpaceX")
		rocket.forward(45)
		rocket.right(90)
		rocket.forward(10)
		rocket.pendown()
		rocket.color("orange")
		rocket.begin_fill()
		rocket.left(105)
		rocket.forward(95)
		rocket.left(150)
		rocket.forward(95)
		rocket.left(105)
		rocket.forward(50)
		rocket.end_fill()
		rocket.left(180)
		rocket.forward(12)
		rocket.begin_fill()
		rocket.color("red")
		rocket.right(75)
		rocket.forward(50)
		rocket.left(150)
		rocket.forward(50)
		rocket.left(105)
		rocket.forward(25)
		rocket.end_fill()
	else:
		tryAgain = turtle.Turtle()
		tryAgain.hideturtle()
		tryAgain.write("Try Again")
		print ("Try over with the all correct answers you will see somthing different! :)")
	
	
		
	
	
    
  
main()
    
