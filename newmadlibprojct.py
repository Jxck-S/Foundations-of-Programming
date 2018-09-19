#Jack Sweeney 9/12/18
def convertToNauticalM(miles):
	 nautical = miles * 0.868976
	 return nautical
def convertToMiles(nautical):
	miles = nautical * 1.15078
	return miles
def convertToMm(inch):
	mM = inch * 25.4
	return mM
	
def convertToInch(mM):
	inch = mM * 0.0393701
	return inch 
	
def main():
	inch = 0
	mM = 0
	nautical = 0
	userGuessMonths = 0
	userGuessMonths = int(input("How long do you think it will take to travel to Mars with Elon Musks new BFR?"))
	
	if( userGuessMonths == 3 or userGuessMonths 2 ):
		print "Elon also thinks it may take 3 to 2 months to get to Mars with his new BFR. He'd like to make it one month."
	elif( userGuessMonths > 3 ):
		print "Elon thinks that its gonna take less than four months to get to Mars with his new BFR but you think othewise."
	elif( userGuessMonths == 1 ):
		print "Wow you must really believe in Elon Musk and his work he'd like to believe itl take one month but he thinks like 2 to 3 months"
		
    
  
main()
    
