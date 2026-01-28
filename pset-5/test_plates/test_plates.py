from plates import is_valid


def test_empty():
	assert is_valid("") == False
	assert is_valid(" ") == False
	assert is_valid("  ") == False
	assert is_valid("    ") == False


def test_starts_with_two_letters():
	assert is_valid("aa") == True
	assert is_valid("Ab") == True
	assert is_valid("Ababab") == True
	assert is_valid("a5a") == False
	assert is_valid("5aa") == False
	assert is_valid("01a") == False


def test_min_max_length():
	assert is_valid("") == False
	assert is_valid("a") == False
	assert is_valid("ab") == True
	assert is_valid("abc") == True
	assert is_valid("abcd") == True
	assert is_valid("abcd") == True
	assert is_valid("abcde") == True
	assert is_valid("abcdef") == True
	assert is_valid("abcdefg") == False
	assert is_valid("qwertyuiopasdfghjklzxcvnmm") == False


def test_for_middle_numbers():
	assert is_valid("cs50a") == False
	assert is_valid("ab1000z") == False


def test_for_first_zero():
	assert is_valid("cs05") == False
	assert is_valid("ab0") == False


def test_punctuation():
	assert is_valid("cs50.") == False
	assert is_valid("cs!50") == False
	assert is_valid("cs'50") == False
	assert is_valid("cs'i50") == False
	assert is_valid("cs$50") == False
	assert is_valid("cs$50") == False
	assert is_valid("cs50#") == False
	assert is_valid("ab3.14") == False

