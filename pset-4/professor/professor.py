import random


def main():
	MAX_TRIES = 3
	MAX_PROBLEMS = 10
	math_problems = []
	current_problem = 0
	score = 0
	tries = 0
	level = get_level()	

	for _ in range(MAX_PROBLEMS):
		p, a = generate_new_problem(level)
		math_problems.append({"problem": p, "answer": a})
	
	while current_problem < MAX_PROBLEMS:
		problem_text = math_problems[current_problem].get("problem")

		try:
			user_answer = int(input(problem_text))
		except ValueError:
			continue

		tries += 1
		correct_answer = math_problems[current_problem].get("answer")

		if user_answer == correct_answer:
			score += 1
			tries = 0
			current_problem += 1
		else:
			print("EEE")
			if tries >= MAX_TRIES:
				print(f"{problem_text}{correct_answer}")
				tries = 0	
				current_problem += 1
				
	print(f"Score: {score}")
			

def get_level():
	while True:
		level = input("Level: ")		 
		if level in list("123"):
			return int(level)


def generate_integer(level):
	start = 0 if level == 1 else 10 ** (level - 1) 
	end = (10 ** level) - 1
	return random.randint(start, end)
	

def generate_new_problem(level):
	x = generate_integer(level)
	y = generate_integer(level)
	problem = f"{x} + {y} = "
	answer = x + y
	return problem, answer
		

if __name__ == "__main__":
    main()
