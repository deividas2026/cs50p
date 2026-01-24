def main():
	time = input("What time is it? ")
	args = time.split()
	arg_len = len(args)	

	if arg_len == 1:
		time = convert(args[0])
	elif arg_len == 2:
		time = convert(args[0], "12", args[1])

	if time >= 7.0 and time <= 8.0:
		print("breakfast time")	
	elif time >= 12.0 and time <= 13.0:
		print("lunch time")
	elif time >= 18.0 and time <= 19.0:
		print("dinner time")


def convert(time, time_format="24", time_period="a.m."):
	t = time.split(":")
	hours = float(t[0])
	minutes = float(t[1])

	if time_format == "12":
		if time_period == "a.m." and hours == 12:
			hours = 0
		if time_period == "p.m." and hours > 0 and hours < 12:
			hours += 12

	return hours + (minutes / 60)



if __name__ == "__main__":
	main()
