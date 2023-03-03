#Higher Order Functions - take other functions as arguments or return them as a result.
#Map returns a new iterable/list with the runction applied to each arg.
#Filter filters an iterable by moving items that do not match a predicate.
#pure functions - has no side effects and return a value that depends only on their arg.
try:
	pin_code = int(input("input: "))
	print(pin_code)
except ValueError:
	print("value Error")
	pass
