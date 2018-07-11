#Jack Sweeney 7/9/18
#Calculator for three items on your wish list with tax and shipping 

def main():
#name
	fName = input("Whats your first name?") 
	lName = input("Whats your last name?")
#Fist Item input
    firstItem = input("Whats the first item your buying?")
    firstItemPrice = float(input("Whats the price of the " + firstItem))
    
#Second Item input
    secondItem = input("Whats the second item your buying?")
    secondItemPrice = float(input("Whats the price of the " + secondItem))
    
#Third Item input
    thirdItem = input("Whats the third item your buying?")
    thirdItemPrice = float(input("Whats the price of the " + thirdItem))
	
#Naming  
	intial = fName[0] + lName[0]
	fullName = fName + " " + lName 
    
#Subtotal Calculation
    subTotal = firstItemPrice + secondItemPrice + thirdItemPrice

#Tax Calculation
    tax = .065 * subTotal 

#Total Calculations
    shipping = 5.99
    total = tax + shipping + subTotal
    
#Output
    print intial + "'s Wish List"
    print "___________________________"
    print "Item                   Cost"
    print "---------------------------"
    print firstItem +  "       $" + str(firstItemPrice)
    print secondItem + "       $" + str(secondItemPrice)
    print thirdItem +  "       $" + str(thirdItemPrice)
    print "==========================="
    print "     Subtotal        $" + str(subTotal)
	print "     Tax             $" + str(tax)
	print "     Shipping        $" + str(shipping)
	print "     Total           $" + str(total)
	print "___________________________"
	print "Good luck saving for your wish list have a great day " + fullName + "!"


    
main()