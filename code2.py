#!/usr/bin/env python3

# Define a function that checks the first letter of a string
def firstletter(word):
    # Returns True if the first letter is 'b' or 's', otherwise False
    return word.startswith(('b', 's'))

def main():
    # Create a list named colours with at least four strings
    colours = ["blue", "yellow", "black", "silver"]

    # Initialize an empty list to store items that match the condition
    result = [color for color in colours if firstletter(color)]

    # Print the result list
    print(result)

# Execute the main block if the script is run directly
if __name__ == "__main__":
    main()

