# The while Loop

import turtle

def main():
    trixie = turtle.Turtle()
    trixie.speed(10)

    answer = "y"
    while(answer == "y"):
        numCircles = int(input("How many circles should be drawn?"))
        diameter = int(input("What is the diameter for the circles?"))
        trixie.color(input("What color is the turtle?"))

        x = 0
        while(x < numCircles):
            trixie.circle(diameter)
            trixie.left(360 / numCircles)
            x = x + 1
        answer = input("Would you like to draw another? y/n ")

main()