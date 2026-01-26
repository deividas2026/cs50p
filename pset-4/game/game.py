import random


def main():
	level = get_level()
	answer = random.randint(1, level)	
	guess(answer)	


def get_level():
	while True:
		try:
			n = int(input("Level: "))
		except ValueError:
			continue
		else:
			if n > 0:
				return n


def guess(answer):
	while True:
		try:
			g = int(input("Guess: "))
		except ValueError:
			continue
		else:
			if g <= 0:
				continue
			
			if g > answer:
				print("Too large!")
			elif g < answer:
				print("Too small!")
			else:
				print("Just right!")
				return


if __name__ == "__main__":
	main()
