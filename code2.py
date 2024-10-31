#!/usr/bin/env python3

def firstletter(word):
    return word[0].lower() in {'b', 's'}

def main():
    colours = ["blue", "red", "green", "silver", "black"]
    result = [color for color in colours if firstletter(color)]
    print(result)

if __name__ == "__main__":
    main()

