
def calculate(a, b, sym):
	if sym == '+':
		return a + b
	elif sym == '-':
		return a - b
	elif sym == '*':
		return a * b
	elif sym == '/':
		if b == 0:
			return 'error'
		else:
			return a / b
	else:
		return 'symbol error'

# def calculate_match_case(a, b, sym):
# 	# python 3.10+
# 	match sym:
# 		case '+':
# 			return a + b
# 		case '-':
# 			return a - b
# 		case '*':
# 			return a * b
# 		case '/':
# 			if b == 0:
# 				return 'error'
# 			else:
# 				return a / b
# 		case _:
# 			return 'error'

def calculate_lambda(a, b ,sym):
	op_func = {
		'+': lambda x, y: x + y,
		'-': lambda x, y: x - y,
		'*': lambda x, y: x * y,
		'/': lambda x, y: 'error' if y == 0 else x / y
	}

	func = op_func.get(sym, lambda x, y: 'symbol error')

	return func(a, b)

def main():
	num1 = float(input("a = "))
	symbol = input("symbol = ")
	num2 = float(input("b = "))
	result = calculate(num1, num2, symbol)
	# result = calculate_match_case(num1, num2, symbol)
	result = calculate_lambda(num1, num2, symbol)

	print(f"{num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
	main()
