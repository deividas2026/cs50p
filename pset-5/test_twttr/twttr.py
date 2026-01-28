def main():
	user_input = input("Input: ")
	print(f"Output: {shorten(user_input)}")
	

def shorten(word):
	vowels = list("aAeEiIuUoO")
	without_vowels = ""
	for character in word:
		if character not in vowels:
			without_vowels += character	
	
	return without_vowels


if __name__ == "__main__":
	main()
