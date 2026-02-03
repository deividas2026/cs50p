import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^([1-9]|1[0-2])(?::(0[0-9]|[1-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::(0[0-9]|[1-5][0-9]))? (AM|PM)$", s.strip().lower(), re.IGNORECASE)

    if matches:
        from_hours, from_minutes, from_daytime, to_hours, to_minutes, to_daytime = matches.groups()
        if from_daytime == to_daytime:
            raise ValueError 

        from_hours = int(from_hours)
        to_hours = int(to_hours)

        if from_daytime == "am" and from_hours == 12:
            from_hours = 0
        elif from_daytime == "pm" and from_hours < 12:
            from_hours += 12

        if to_daytime == "am" and to_hours == 12:
            to_hours = 0
        elif to_daytime == "pm" and to_hours < 12:
            to_hours += 12

        if from_minutes is None:
            from_minutes = 0
        
        if to_minutes is None:
            to_minutes = 0

        return f"{from_hours:02}:{from_minutes:02} to {to_hours:02}:{to_minutes:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
