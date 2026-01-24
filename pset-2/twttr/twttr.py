vowels = ["a", "e", "i", "u", "o"]
str_with_vowels = input("Input: ")
str_without_vowels = ""

for c in str_with_vowels:
	if c.lower() not in vowels:
		str_without_vowels += c	
	
print(f"Output: {str_without_vowels}")
