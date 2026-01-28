def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
	if len(s) > 6 or len(s) < 2:
		return False

	if not s[:2].isalpha():
		return False

	contains_digits = False
	for c in s[2:]:
		if c.isdigit():
			if not contains_digits and c == "0":
				return False
			contains_digits = True
		elif not c.isalpha():
			return False
		elif c.isalpha() and contains_digits:
			return False

	return True


if __name__ == "__main__":
	main()
