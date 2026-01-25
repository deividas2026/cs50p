months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
	while True:
		date = input("Date: ").strip()
		date_validated = validate_date(date)
		if date_validated:
			break	
	
	if date_validated == "LONG":
		month, day, year = date.split()
		m = months.index(month) + 1
		d = int(day[:-1])
		y = int(year)
		print(f"{y:04}-{m:02}-{d:02}")
	else:
		month, day, year = date.split("/")
		m = int(month)
		d = int(day)
		y = int(year)
		print(f"{y:04}-{m:02}-{d:02}")
			

def validate_date(d):
	m_valid = False
	d_valid = False
	y_valid = False

	long_date_args = d.split()	
	if len(long_date_args) == 3:
		month, day, year = long_date_args	

		if month.isalpha() and month.title() in months:
			m_valid = True	

		if day[:-1].isdigit() and day[-1:] == "," and int(day[:-1]) > 0 and int(day[:-1]) < 32:
			d_valid = True

		if year.isdigit() and int(year) >= 0:
			y_valid = True

		if m_valid and d_valid and y_valid:
			return "LONG"
		else:
			return None

	
	short_date_args = d.split("/")
	if len(short_date_args) == 3:
		month, day, year = short_date_args
		
		if month.isdigit() and int(month) > 0 and int(month) < 13:
			m_valid = True
		if day.isdigit() and int(day) > 0 and int(day) < 32:
			d_valid = True
		if year.isdigit() and int(year) >= 0:
			y_valid = True

		if m_valid and d_valid and y_valid:
			return "SHORT"
		else:
			return None
		
	return None

	
main()
