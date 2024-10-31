#!/usr/bin/env python3

# Define a function to check the first letter of a string
def firstletter(word):
    return word[0].lower() in {'b', 's'}  # Returns True if the first letter is 'b' or 's'

def main():
    # Create an indexable, mutable iterable with at least four colors
    colours = ["blue", "red", "green", "silver", "black"]
    
    # Use list comprehension to apply firstletter function to each item in colours
    result = [colour for colour in colours if firstletter(colour)]
    
    # Print the result list
    print(result)

# Run the main block
if __name__ == "__main__":
    main()
