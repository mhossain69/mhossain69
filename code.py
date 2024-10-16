
#!/usr/bin/env python3

def firstletter(word):
    """Check if the first letter is 'b' or 's'."""
    if word[0].lower() in ['b', 's']:
        return True
    return False

def main():
    # Create a mutable, indexable list of colours
    colours = ['blue', 'green', 'red', 'silver']

    # Create an empty list to store results
    result = []

    # Check each colour with the firstletter function
    for colour in colours:
        if firstletter(colour):
            result.append(colour)

    # Print the result list
    print(result)

# Main block
if __name__ == "__main__":
    main()
