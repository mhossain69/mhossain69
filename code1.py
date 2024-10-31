#!/usr/bin/env python3

def firstletter(string):
    """Check if the first letter of the string is 'b' or 's'."""
    first_char = string[0].lower()  # Make it case insensitive
    if first_char == 'b' or first_char == 's':
        return True
    return False

def main():
    # Create a mutable, indexable iterable named colours with at least four strings
    colours = ["blue", "green", "yellow", "silver", "black"]

    # Create an empty list to hold results
    result = []

    # Call firstletter for each item in colours and add to result if True
    for colour in colours:
        if firstletter(colour):
            result.append(colour)

    # Print the result list
    print(result)

if __name__ == "__main__":
    main()

