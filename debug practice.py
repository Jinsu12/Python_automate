#Calculator

#Add
def add(n1, n2):
	return n1+n2

#Subtract
def subtract(n1, n2):
	return n1-n2

#Multiply
def multiply(n1, n2):
	return n1*n2

#Divide
def divide(n1,n2):
	return n1/n2

operations = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide
}

num1 = int(input("What is the first number? : "))
for symbol in operations:
	print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number? : "))


calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What is the next number? : "))
second_answer = calculation_function(calculation_function(num1,num2),num3)

print(f"{first_answer}{operation_symbol}{num3}={second_answer}")