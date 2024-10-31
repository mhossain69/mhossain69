Question 3:

#!/usr/bin/env python3
# Main block for script - Lab Investigation 1, Part 1

import sys

def calculate_vowel_percentage(word: str) -> float:
    """Calculates the percentage of vowels in a given word."""
    vowels = set("aeiouAEIOU")
    total_vowels = len([char for char in word if char in vowels])
    return total_vowels / len(word) if word else 0.0  # Return 0.0 if the word length is 0

def main():
    # Collect command line arguments, excluding the filename - Lab Investigation 2, Part 2
    args = sys.argv[1:]

    # Check for no arguments and handle accordingly - Lab Investigation 3, Part 3
    if not args:
        print("No args!")  # Conditional statement - Lab Investigation 3, Part 3
        return

    # Iterate over each argument and calculate vowel percentage - Lab Investigation 4, Part 4
    results = [(word, calculate_vowel_percentage(word)) for word in args]
    for word, percent in results:
        print(f"Word: {word} Percent {percent:.6f}")

# Execute main block
if __name__ == "__main__":
    main()

