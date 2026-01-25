names = []

while True:
	try:
		name = input("Name: ")
	except EOFError:
		print()
		break
	else:
		names.append(name)

output = "Adieu, adieu, to "
if len(names) == 1:
	output += names[0]	
elif len(names) == 2:
	output +=  " and ".join(names)
elif len(names) > 2:
	output += ", ".join(names[:-1]) + ", and " + names[-1]

print(output)
