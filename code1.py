#!/usr/bin/env python3
import sys

def read_file(filename: str) -> list:
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return ['File not found!']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: no file specified.")
    else:
        filename = sys.argv[1]
        lines = read_file(filename)
        for line in lines:
            print(line, end="")
        print(f"\nNumber of lines: {len(lines)}")
