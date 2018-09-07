class Antivirus:
    # Antivirus class represents the facts related to a Antivirus.
	def __init__(self, name = "", strengthPts = 0, powerUps = 0, motto = ""):
    # Create a new Antivirus with a name and other attributes
		self.name = name 
		self.strengthPts = strengthPts
		self.powerUps = powerUps
		self.motto = motto
	def addStrengthPts(self, points):
	# Adds points to the Antivirus's strength.
		self.strengthPts = self.strengthPts + points
	def addPowerUps(self, powers):
	#Add power ups to the Antivirus	
		self.powerUps = self.powerUps + powers
	
def main():

	norton = Antivirus("Mr.Norton AntiVirus", 15, 0, "If the computer is without me their is no working computer" )
	print "Let me tell you about " + norton.name + " his motto is " + norton.motto + "!"
	print "One day " + norton.name + " found one of his enemies Dr.CrptoLocker attacking a victim computer!"
	print norton.name + " Was up for a fight with Dr.CrptoLocker the only thing is that " + norton.name + " had " + str(norton.powerUps) + " Power ups."
	print norton.name + " Does has a high strenght thought at " + str(norton.strengthPts) + " points!"
	print "Dr.CrptoLocker has a powerful powerup to freeze " + norton.name + " for a small amount of time but only has 8 points."
	print norton.name + "takes down Dr.CrptoLocker."
	norton.addPowerUps(1)
	norton.addStrengthPts(2)
	print norton.name + " Gains 2 strenght points he also gained one powerup for defeating Dr.CryptoLocker!"
	print norton.name + " now has " + str(norton.powerUps) + " power up and "  + str(norton.strengthPts) + " strengh points left to take down others!"
main()