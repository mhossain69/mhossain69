
#!/usr/bin/env python3

def firstletter(word):
    # Get the first letter of the string and check if it's 'b' or 's'
    if word[0].lower() in ['b', 's']:
        return True
    else:
        return False

if __name__ == "__main__":
    # Create a mutable, indexable iterable called colours
    colours = ["blue", "red", "green", "silver"]
    
    # Initialize an empty list to store the results
    result = []
    
    # Call the firstletter function for each item in colours
    for colour in colours:
        if firstletter(colour):
            result.append(colour)
    
    # Print the result list
    print(result)
