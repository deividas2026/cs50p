import sys
import os


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[-1]
    if not filename.endswith(".py"):
        sys.exit(f"File has to have a python extension: {filename}")

    lines = 0
    try:
        with open(filename) as file:
            for line in file:
                stripped = line.lstrip()
                if len(stripped) == 0 or stripped.startswith("#"):
                    continue
                lines += 1
    except OSError as e:
        sys.exit(
            f"Error occured while trying to open '{filename}': {os.strerror(e.errno)}"
        )
    else:
        print(lines)


if __name__ == "__main__":
    main()
