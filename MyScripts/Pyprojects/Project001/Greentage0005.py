#Grading system
#Input your marks and know your Grade
x = int(input("Enter your Marks: "))

if x >= 70 and x <= 100:
	print("Grade A")
elif x >= 60 and x <= 69:
	print("Grade B")
elif x >= 50 and x <= 59:
	print("Grade C")
elif x >= 40 and x <= 49:
	print("Grade D")
elif x >= 1 and x <= 39:
	print("Grade E")
else:
	print("Missing grade")

