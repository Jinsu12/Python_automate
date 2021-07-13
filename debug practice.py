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

operation_symbol = input("Pick another operation: ")  # operation symbol을 사용한 후에 이것을 불러주는 라인이 없었다.
num3 = int(input("What is the next number? : "))
calculation_function = operations[operation_symbol]  # operation을 불러주는 함수를 쓰고
second_answer = calculation_function(first_answer, num3)  # operation을 새로 불렀기 때문에 겹치지 않겠? first_answer로 바꿔준다
print(f"{first_answer}{operation_symbol}{num3}={second_answer}")

go_stop = False

while not go_stop:
	end_of_game = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to exit.:")
	if end_of_game == 'y':
		operation_symbol = input("Pick another operation: ")  # operation symbol을 사용한 후에 이것을 불러주는 라인이 없었다.
		num3 = int(input("What is the next number? : "))
		calculation_function = operations[operation_symbol]  # operation을 불러주는 함수를 쓰고
		second_answer = calculation_function(second_answer, num3)  # operation을 새로 불렀기 때문에 겹치지 않겠? first_answer로 바꿔준다
		print(f"{first_answer}{operation_symbol}{num3}={second_answer}")
	elif end_of_game == 'n':
		break
