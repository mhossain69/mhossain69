#!/usr/bin/env python3

import sys

def read_file(filename: str) -> list:
    """
    Open a file, return contents as a list of lines.
    Return a message if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return ["File not found!"]

if __name__ == "__main__":
    # Check if the script has been provided with a filename as a command-line argument
    if len(sys.argv) < 2:
        print("Error: no file specified.")
    else:
        # Get the filename from the command-line arguments
        filename = sys.argv[1]
        # Read the file content
        content = read_file(filename)
        # Print each line in the file content
        for line in content:
            print(line, end='')
        # Print the number of lines in the content
        print(f"\nNumber of lines: {len(content)}")
