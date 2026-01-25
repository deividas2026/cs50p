def main():
	fuel_left = get_fuel_left()	
	if fuel_left >= 99:
		print("F")
	elif fuel_left <= 1:
		print("E")
	else:
		print(f"{fuel_left}%")


def get_fuel_left():
	while True:
		fraction = input("Fraction: ")
		fraction = fraction.split("/")

		try:
			x = int(fraction[0])
			y = int(fraction[1])	
		except (ValueError, IndexError):
			pass
		else:
			if x >= 0 and y > 0 and y >= x:
				break
		
	return round((x / y) * 100)


main()
