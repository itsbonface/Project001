
#Task:
#In a plane of 34 sits calculate the total cost of all plane tickets, each @5,000KSh. Children tickets are free.

#Challange:
#How to handle ValueError or NameError for the inputs.
#I tried this but it did not work:

sit = 0
ticket = 5000
for sit in range(1,35):
	print("This is sit Number", sit)
	sit -= 1
	while True:
		try:
			age = int(input("What is your age: "))
			name = str(input("What is your name: "))
		except ValueError:
			print("Oops!!\nPlease try an integer(ie. 23).")
			pass
		except NameError:
			print("Word input is required(ie. Sandra).")
			pass
		print(str(ticket) + ".00KSh")
		ticket += 5000

		if age <= 5:
			print("Children tickets are free", name,". Enjoy your free ride...")
			continue

		print("That is the total cost is" + str(ticket) + ".00KSh")


"""
sit = 0
ticket = 5000
for sit in range(1,35):
	print("This is sit Number", sit)
	sit -= 1
	age = int(input("What is your age: "))
	name = str(input("What is your name: "))
	if age <= 5:
		print("Children tickets are free", name,". Enjoy your free ride...")
		continue
	print(str(ticket) + ".00KSh")
	ticket += 5000

print("That is the total cost is" + str(ticket-5000) + ".00KSh")
"""