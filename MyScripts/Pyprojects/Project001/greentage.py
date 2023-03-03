#Working with inputs.
name = input("Name: ")
age = input("age: ")
reg_number = input("Registration Number: ")

print("Your name is " + name + ". You are " + age + "years old and\n your Registration Number is " + reg_number + ".")

import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,])
b = a.reshape(3,3)

print(b)