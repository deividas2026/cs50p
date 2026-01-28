from twttr import shorten


def test_shorten_empty():
	assert shorten("") == ""
	assert shorten(" ") == " "


def test_shorten_trailing_and_leading_spaces():
	assert shorten("cs50 ") == "cs50 "
	assert shorten(" cs50") == " cs50"
	assert shorten(" cs50 ") == " cs50 "


def test_shorten_with_no_vowels():
	assert shorten("Rhythm") == "Rhythm"
	assert shorten("MyTH") == "MyTH"
	assert shorten("q Q w W r R t T y Y zxcvbnm") == "q Q w W r R t T y Y zxcvbnm"


def test_shorten_with_vowels():
	assert shorten("Hello, World!") == "Hll, Wrld!"
	assert shorten("AeIuO is not AEIUO") == " s nt "
	assert shorten("C@ts ARE not DOGS") == "C@ts R nt DGS"
