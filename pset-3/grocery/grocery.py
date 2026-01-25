grocery_list = {}

while True:
	try:
		grocery = input().upper()
	except EOFError:
		print()
		break
	else:
		grocery_list[grocery] = grocery_list.get(grocery, 0) + 1

for grocery, count in sorted(grocery_list.items()):
	print(f"{count} {grocery}")
