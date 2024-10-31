Question 3: 

#!/usr/bin/env python3
# Main block for script - Lab Investigation 1, Part 1

def vowel_percent(word: str) -> float:
    """returns the percent of the word that is vowels for a given word"""
    # Count vowels and calculate percentage - Lab Investigation 2, Part 2
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in word if char in vowels)
    return vowel_count / len(word) if len(word) > 0 else 0.0

if __name__ == "__main__":
    # Collect command line arguments, excluding the filename - Lab Investigation 2, Part 2
    import sys
    args = sys.argv[1:]
    
    # Check for no arguments and handle accordingly - Lab Investigation 3, Part 3
    if len(args) == 0:
        print("No args!")  # Conditional statement - Lab Investigation 3, Part 3
        sys.exit(0)
    
    # Iterate over each argument and calculate vowel percentage - Lab Investigation 4, Part 4
    for word in args:
        percent = vowel_percent(word)
        print(f"Word: {word} Percent {percent}")

