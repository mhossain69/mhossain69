#!/usr/bin/env python3

def firstletter(word):
    # Returns True if the first letter is 'b' or 's', else False
    return word.startswith(('b', 's'))

def main():
    # Create a list of colours with at least four strings
    colours = ["blue", "yellow", "scarlet", "purple"]

    # Use list comprehension to call firstletter and filter matching items
    result = [color for color in colours if firstletter(color)]
    
    # Print the result list
    print(result)

# Execute main block when script runs directly
if __name__ == "__main__":
    main()

