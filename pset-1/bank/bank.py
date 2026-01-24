greeting = input("Greeting: ").lower().strip()
starts_with_hello = greeting.startswith("hello")

if starts_with_hello:
	print("$0")
elif greeting[0] == "h":
	print("$20")
else:
	print("$100")
