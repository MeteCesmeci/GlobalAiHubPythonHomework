#Turkish Ai Hub Introduction to Python Programming course
#Homework 1
#Printing entered values and types of values
#Student Name: Mete Çeşmeci
print("Enter 5 values one by one.")
value1 = int(input("Enter value #1 as integer: "))
value2 = float(input("Enter value #2 as float: "))
value3 = input("Enter value #3 as string: ")
value4 = bool(input("Enter value #4 as boolean: "))
value5 = tuple(input("Enter value #5 as tuple: "))

print("\nResults")
print(f'Value #1 is {value1}')
print("Value: {} ,Type: {}".format(value1, type(value1)))
print(f'Value #2 is {value2}')
print("Value: {} ,Type: {}".format(value2, type(value2)))
print(f'Value #3 is {value3}')
print("Value: {} ,Type: {}".format(value3, type(value3)))
print(f'Value #4 is {value4}')
print("Value: {} ,Type: {}".format(value4, type(value4)))
print(f'Value #5 is {value5}')
print("Value: {} ,Type: {}".format(value5, type(value5)))
