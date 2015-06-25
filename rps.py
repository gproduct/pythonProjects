import random
import sys
def main( str ):
	userItem = raw_input("Please choose between rock,paper or scissors(r/p/s): ")
	items = ['rock','paper','scissors']
	compRand = random.choice(items)
	print "The computer has chosen",compRand
	if compRand == 'paper':
		if userItem == 's':
			print "You win!"
			playAgain = raw_input("Play again? (y/n) ") 
			if playAgain == 'y':
				main(0)
			elif playAgain == 'n':
				sys.exit()
		elif userItem == 'r':
			print "Noob!"
			playAgain = raw_input("Play again? (y/n) ") 
			if playAgain == 'y':
				main(0)
			elif playAgain == 'n':
				sys.exit()
		elif userItem == 'p':
			print "DRAW"
			main(0)
	elif compRand == 'rock':
		if userItem == 's':
			print "Noob"
			playAgain = raw_input("Play again? (y/n) ") 
			if playAgain == 'y':
				main(0)
			elif playAgain == 'n':
				sys.exit()
		elif userItem == 'r':
			print "DRAW"
			playAgain = raw_input("Play again? (y/n) ") 
			if playAgain == 'y':
				main(0)
			elif playAgain == 'n':
				sys.exit()
			main(0)
		elif userItem == 'p':
			print "You win!"
			playAgain = raw_input("Play again? (y/n) ") 
			if playAgain == 'y':
				main(0)
			elif playAgain == 'n':
				sys.exit()
	elif compRand == 'scissors':
		if userItem == 's':
			print "DRAW"
			main(0)
		elif userItem == 'r':
			print "You win"
			playAgain = raw_input("Play again? (y/n) ") 
			if playAgain == 'y':
				main(0)
			elif playAgain == 'n':
				sys.exit()
		elif userItem == 'p':
			print "Noob"
			playAgain = raw_input("Play again? (y/n) ") 
			if playAgain == 'y':
				main(0)
			elif playAgain == 'n':
				sys.exit()
print "Welcome to rock,paper,scissors!"
main(0)
#working