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


# input을 한번 한거는 다시 인풋하더라도 바뀌지 않는지?

operation_symbol2 = input("Pick another operation: ")
num3 = int(input("What is the next number? : "))
calculation_function2 = operations[operation_symbol2]

second_answer = calculation_function2(calculation_function(num1,num2),num3)

print(f"{first_answer}{operation_symbol2}{num3}={second_answer}")