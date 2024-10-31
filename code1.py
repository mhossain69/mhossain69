#!/usr/bin/env python3

def firstletter(word):
    """Check if the first letter of the word is 'b' or 's'."""
    return word[0].lower() in ['b', 's']

def main():
    # Create a mutable, indexable iterable with at least four strings
    colours = ["blue", "green", "red", "salmon"]
    
    # Initialize an empty list to store results
    result = []
    
    # Call firstletter with each item of colours and add to result if True
    for color in colours:
        if firstletter(color):
            result.append(color)
    
    # Print the result list
    print(result)

# Ensure the main block runs only if the script is executed directly
if __name__ == "__main__":
    main()

