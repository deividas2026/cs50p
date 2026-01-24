expression = input("Expression: ").split()
x_operand = float(expression[0])
y_operator = expression[1]
z_operand = float(expression[2])

match y_operator:
	case "+":
		result = x_operand + z_operand
	case "-":
		result = x_operand - z_operand
	case "*":
		result = x_operand * z_operand
	case "/":
		result = x_operand / z_operand
	case _:
		result = "Invalid operator"

print(result)
