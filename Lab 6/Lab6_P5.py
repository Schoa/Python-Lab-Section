def analyze_words(words):
    result = []
    
    for index, word in enumerate(words):
        # Create a list to hold character counts (assuming only lowercase letters)
        frequency = [0] * 26  # For 'a' to 'z'
        
        # Count character frequencies
        for char in word:
            if 'a' <= char <= 'z':  # Only count lowercase letters
                frequency[ord(char) - ord('a')] += 1
        
        # Create a sorted list of "character: count" strings
        frequency_list = [f"{chr(i + ord('a'))}: {frequency[i]}" for i in range(26) if frequency[i] > 0]
        
        # Format the output string with the word index
        result_string = f"{index} - {', '.join(frequency_list)}"
        result.append(result_string)
    
    return result

# Read input
n = int(input())
words = input().split()  # Read n space-separated strings

# Call the function and get the result
analyzed_words = analyze_words(words)

# Print each result on a new line
for line in analyzed_words:
    print(line)