import sys

def main( str ):
	xInt = input("How many number do you want to enter?Max 10")
	x = int(xInt)
	numbers = []
	maxLength = 10
	done = 1
	while len(numbers) < maxLength and done == 1:
		num = raw_input("Enter! ")
		if num == 'done':
			done = 0
		else:
			numbers.append(num)
			print numbers
	print "We gathered your information"
	allNumbers = map(float, numbers)
	#print allNumbers
	sumNums = sum(allNumbers)
	result = sumNums / len(allNumbers)
	print "The result is ", result
	restart = raw_input("Use again? (y/n)")
	if restart == 'y':
		main(0)
	elif restart == 'n':
		sys.exit()


print "WELCOME TO AVERAGE CALCULATOR!"
main(0)
#working

		


	