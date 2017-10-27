import random

var = 1
secret = random.randint(1,1000+1)
while var == 1 :


	number = input("Please enter a number 1 through 1,000:")
	number = int(number)

	print(secret)
	if(number > secret):
		print("too high, not in range")
	elif(number < secret):
		print("too low, not in range")
	if(number == secret):
		print("you won!!!")
		var = 0
