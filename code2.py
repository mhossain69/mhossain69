#!/usr/bin/env python3
import sys

def read_file(filename: str) -> list:
    """Open a file and return its contents line-by-line. Return an error message if file is not found."""
    try:
        with open(filename, 'r') as file:
            return [line.rstrip('\n') for line in file]  # Remove newline characters from each line
    except FileNotFoundError:
        return ["File not found!"]

def main():
    """Main function to handle command-line arguments and file output."""
    if len(sys.argv) < 2:
        print("Error: no file specified.")
        return

    filename = sys.argv[1]
    lines = read_file(filename)

    for line in lines:
        print(line)
    print(f"\nNumber of lines: {len(lines)}")

if __name__ == "__main__":
    main()
