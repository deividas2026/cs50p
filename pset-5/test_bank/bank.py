def main():
	greeting = input("Greeting: ")
	print(f"${value(greeting)}")	


def value(greeting):
	if greeting.lower().startswith("hello"):
		value = 0
	elif greeting.lower()[0] == "h":
		value = 20
	else:
		value = 100
		
	return value


if __name__ == "__main__":
	main()
