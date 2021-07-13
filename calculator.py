def add(n1, n2):
	return n1 + n2
def subtract(n1, n2):
	return n1 - n2
def divide(n1, n2):
	return n1 / n2
def multiply(n1, n2):
	return n1 * n2


operation = {
	'+': add,
	'-': subtract,
	'/': divide,
	'*': multiply
}

def restart():
	num1 = float(input("What is the first number? >> "))
	for i in operation:
		print(i)

	go = True
	while go:
		op_choice = input("Choose the operation >> ")
		num2 = float(input("What is the next number? >> "))
		result = operation[op_choice]
		result2 = result(num1, num2)
		print(f"{num1} {op_choice} {num2} = {result2}")
		continue_restart = input("Would you like to continue 'y' or restart 'n'? >> ")
		if continue_restart == 'n':
			go = False
			restart()
		else:
			True
restart()