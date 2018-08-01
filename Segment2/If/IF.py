# The if Statement

def main():

    print("Let's go to the Movies!")

    ticketCost = 7.25
    snackCost = 0.00

    orderPopcorn = input("Popcorn (y or n): ")
    if(orderPopcorn == "y"):
        snackCost = snackCost + 3.75

    totalCost = ticketCost + snackCost

    print ("Cost of Ticket: $" + str(ticketCost))
    print ("Cost of Snacks: $" + str(snackCost))
    print ("Total Cost: $" + str(totalCost))

main()