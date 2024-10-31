#!/usr/bin/env python3

def firstletter(word):
    """Returns True if the first letter of the word is 'b' or 's'."""
    first_char = word[0].lower()
    return first_char == 'b' or first_char == 's'

def main():
    # Define an indexable, mutable iterable with at least four strings
    colours = ["blue", "red", "green", "silver"]

    # Initialize an empty list to store results
    result = []

    # Call firstletter function with each item of colours
    for color in colours:
        if firstletter(color):
            result.append(color)

    # Print the result list
    print(result)

if __name__ == "__main__":
    main()

