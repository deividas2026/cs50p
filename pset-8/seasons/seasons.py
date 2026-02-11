import re
import sys
import inflect
from datetime import date


def main():
    p = inflect.engine()
    date_of_birth = input("Date of Birth: ").strip()

    valid = re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_of_birth)
    if not valid:
        sys.exit("Invalid date")
 
    try:
        days_between = (date.today() - date.fromisoformat(date_of_birth)).days
    except ValueError:
        sys.exit("Invalid date")

    if days_between < 0:
        sys.exit("Invalid date")

    minutes = days_between * 24 * 60
    print(p.number_to_words(minutes, andword="").capitalize(), p.plural_noun("minute", minutes))
    

if __name__ == "__main__":
    main()
