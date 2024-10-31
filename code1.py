#!/usr/bin/env python3

def firstletter(word):
    # Get the first letter of the word
    first = word[0].lower()
    # Check if the first letter is 'b' or 's'
    if first == 'b' or first == 's':
        return True
    return False

def main():
    # Create an indexable, mutable list named colours with at least four strings
    colours = ["blue", "red", "green", "silver", "black"]
    
    # Initialize an empty list to store results
    result = []
    
    # Iterate over each color in colours and check with firstletter function
    for color in colours:
        if firstletter(color):
            result.append(color)
    
    # Print the result list
    print(result)

# Run the main function
if __name__ == "__main__":
    main()

