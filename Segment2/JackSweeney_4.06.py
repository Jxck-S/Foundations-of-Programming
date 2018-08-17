#Jack Sweeney 8/17/18
#Program is meant to see if your eligible to join Programmers of America.

def main():

    age = int(input("How old are you?"))
	gpa = float(input("What is your current GPA? (in .0 format)"))
	programKnow = input("Do u know a programing language? (y or n)")

	
	passStatus = "No"
    if( age >= 15 and gpa >= 3.0 and programKnow == "y" ):
        passStatus = "Yes"
		
    agePass = "Yes"   
    if( age < 15 ):
        agePass = "No"
	
	gpaPass = "Yes"
	if( gpa < 3.0 ):
		gpaPass = "No"
		
	programPass = "Yes"
	if( programKnow == "n" ):
		programPass = "No"
		
	requirements = ["Age >= 15", "GPA >= 3.0", "Know a programing language"]
	
		
	print "________________________________"
	print "Heres your Application Status"
	print "Able to Join Programs of America?"
	print passStatus 
	print "---------------------------------"
	print "Requirement   Status Good?   Entry"
	print "---------------------------------"
	print " Age >= 15    " + agePass + "            " + str(age)
	print " GPA >= 3.0   " + gpaPass + "             " + str(gpa)
	print " Know a       " + programPass + "             " + programKnow
	print " programing  "
	print " language "
	print "_________________________________"
	if ( passStatus == "Yes" ): 
		print "Were glad your able to join our club and help Programmers of America expand!" 
	elif ( passStatus == "No" ):
		print "Sorry you can't join us you don't meat the below requirements."
		print requirements
main()