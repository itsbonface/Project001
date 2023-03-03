#Number guessing
#Choose a random number and the program will tell you if it's right or wrong!!
import random as r

name = input("What's your name? ")
print("welcome to this game " + name)

number = r.randrange(100)
guess = 4

while guess >= 0:
	trial = int(input("Guess my age "))

	def check(x):
		if trial == x:
			print("You won!! ")
		elif trial > x:
			print("Try again!! You are going far. ")
		else:
			print("Try again " + name + ", don't give up. ")

	if guess > 1:
		check(number)
	elif guess == 1:
		check(number)
		print("Okay last chance buddy!! ")
	else:
		print("You lost!!")
	
	guess -= 1
