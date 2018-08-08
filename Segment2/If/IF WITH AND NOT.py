# Logical Operators

def main():

    level = 22
    hiddenCharacter = "yes"
    message = ""

    if( level >= 25 and hiddenCharacter == "yes"):
        message = "Congratulations! You unlocked the Sherlock achievement."
    elif( level >= 25 and not( hiddenCharacter == "yes") ):
        message = "You missed your chance to earn the Sherlock achievement."
    elif( level < 25 and hiddenCharacter == "yes" ):
        message = "You will earn your next achievement when level 25 is complete."    
    else:
        message = "Keep looking for the hidden character."
        
    print("Your level is " + str(level) + ".")
    print(message)

main()