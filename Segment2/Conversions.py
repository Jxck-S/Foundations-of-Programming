#Jack Sweeney 9/12/18
#Used to convert measurements Including inches, mm, Miles, nautical miles
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
	miles = 0
	choiceMilesOrInch = input("Do you want convert between Inches and Milimeters(1) or between Miles and Nautical Miles(2)")
	
	if( choiceMilesOrInch == "1" ):
		choiceMmOrInch = input("Do you Want to convert to Milimemeters(M) or To Inches(I)")
		#convert Inches to mm
		if( choiceMmOrInch == "m" or choiceMmOrInch == "M" ):
			inch = float(input("Enter Inches to be converted to milimeters."))
			print str(inch) + " inches is equal to " + str( convertToMm(inch) ) + " milimeters."
			#Convert Mm to inches
		elif( choiceMmOrInch == "i" or choiceMmOrInch == "I" ):
			mM = float(input("Enter milimeters to be converted to inches."))
			print str(mM) + " milimeters is equal to " + str( convertToInch(mM) ) + " inches."
	elif( choiceMilesOrInch == "2" ):
		choiceNOrM = input("Do you Want to convert to Nautical Miles(N) or To Miles(M)")
		
		#Convert To Miles to Nautical
		if( choiceNOrM == "n" or choiceNOrM == "N" ):
			miles = float(input("Enter miles to be converted to nautical miles."))
			print str(miles) + " miles is equal to " + str( convertToNauticalM(miles) ) + " nautical miles."
			
		#Convert from Nautical to Miles
		elif( choiceNOrM == "m" or choiceNOrM == "M" ):
			nautical = float(input("Enter nautical miles to be converted to miles."))
			print str(nautical) + " nautical miles is equal to " + str( convertToMiles(nautical) ) + " miles."
		
    
  
main()
    
