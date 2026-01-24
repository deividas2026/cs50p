camel_case_input = input("camelCase: ")
snake_case_output = ""

for c in camel_case_input:
	if c.isupper():
		snake_case_output += "_" + c.lower()
	else:
		snake_case_output += c

print(snake_case_output)
