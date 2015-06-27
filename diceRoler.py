import time
from random import randint
import sys

def main(str):
	spinning = 0
	spinOption = 'stop'

	spinOption = raw_input("Type start to start spinning")
	if spinOption == 'start':
		spinning = 1
	else:
		print "FAK JU"
	while spinning == 1:
		for i in range(0,5):
			print "Spinning"
			time.sleep(1)
		askStop = raw_input("Stop it?")
		if askStop == 'stop':
			spinning = 0
			random = randint(0,6)
			print "The dice was ", random
			playAgain = raw_input("Spin it again?(y/n)")
			if playAgain == 'y':
				main(1)
			elif playAgain == 'n':
				sys.exit()




print "Welcome to dice rolling"
main(1)
