#Jack Sweeney 8/29/18
#Asks a user what they think a phrase is then prints their guess and prints the encoded and decoded version of the actual phrase . 
def main():
	secretPhrase = "When something is important enough, you do it even if the odds are not in your favor.-Elon Musk"
	userGuess = input("What do you think the secret phrase is?")
		
	secretPhraseEncoded = []
	secretPhraseDecoded = []
	#Encoding Original
	for m in secretPhrase:
				secretPhraseEncoded.append(ord(m))
	#Decoding Encoded 
	for d in secretPhraseEncoded:
				secretPhraseDecoded.append(chr(m))

	print "Your Guess: " + userGuess
	print "Encoded Phrase: " + str(secretPhraseEncoded)
	print "Decoded Phrase: " + "".join(map(str,secretPhraseDecoded))
	

main()