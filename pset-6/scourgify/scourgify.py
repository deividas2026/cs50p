import csv
import sys

argc = len(sys.argv)
if argc < 3:
    sys.exit("Too few command-line arguments")
elif argc > 3:
    sys.exit("Too many command-line arguments") 
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Both input and output files have to have .csv extension")

input_filename = sys.argv[1]
output_filename = sys.argv[2]
students = []

try:
    with open(input_filename) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            lastname, firstname = row["name"].split(", ")
            student = {"first": firstname, "last": lastname, "house": row["house"]}
            students.append(student)
except csv.Error as e:
    sys.exit(f"CSV error: {e}")
except OSError:
    sys.exit(f"Could not read {input_filename}") 

try:
    with open(output_filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        #for student in sorted(students, key=lambda student: (student["house"], student["first"])):
        for student in students:
            writer.writerow(student)
except csv.Error as e:
    sys.exit(f"CSV error: {e}")
except OSError:
    sys.exit(f"Could not write {output_filename}") 
