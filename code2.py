#!/usr/bin/env python3

import sys

def read_file(filename: str) -> list:
    """
    Open a file and return its contents as a list of lines.
    Return a message if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            # Read and strip trailing newline characters from each line
            return [line.rstrip('\n') for line in file]
    except FileNotFoundError:
        return ["File not found!"]

def main():
    # Check if a filename argument was provided
    if len(sys.argv) < 2:
        print("Error: no file specified.")
        return

    filename = sys.argv[1]
    # Read file contents
    content = read_file(filename)
    # Print each line from the file
    for line in content:
        print(line)
    # Print the number of lines
    print(f"\nNumber of lines: {len(content)}")

if __name__ == "__main__":
    main()
