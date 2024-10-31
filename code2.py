#!/usr/bin/env python3

def firstletter(string):
    """Check if the first letter of the string is 'b' or 's'."""
    return string[0].lower() in ['b', 's']

def main():
    # Define a mutable, indexable iterable with at least four strings
    colours = ["blue", "green", "yellow", "silver", "black"]

    # Use list comprehension to filter colours based on the first letter
    result = [colour for colour in colours if firstletter(colour)]

    # Print the result list
    print(result)

if __name__ == "__main__":
    main()

