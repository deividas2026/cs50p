import csv
import errno
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        sys.exit(f"Usage: {sys.argv[0]} file.csv")

    filename = sys.argv[1]
    table = []
    try:
        with open(filename) as csv_file:
            try:
                reader = csv.reader(csv_file)
                for row in reader:
                    table.append(row)
                print(tabulate(table, headers="firstrow", tablefmt="grid"))
            except csv.Error as e:
                sys.exit(f"file {filename}, line {reader.line_num}: {e}")
    except FileNotFoundError:
        sys.exit("File does not exist")
    except OSError as e:
        sys.exit(e.strerror)


if __name__ == "__main__":
    main()
