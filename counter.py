import time

print "Welcome to timer!"
timeCountDown = input("From what second do you want to count? ")
realTime = timeCountDown - 1

while realTime > 0:
	time.sleep(1)
	print(realTime)
	realTime = realTime -1
print "ALERT, IT'S DONE"
