def count_word_frequencies(text):
    # Create a dictionary to hold word frequencies
    Bibliothek = {}

    # Convert the text to lowercase and split it into words
    words = text.lower().split()

    # Count frequency of each word
    for word in words:
        if word in Bibliothek:
            Bibliothek[word] += 1
        else:
            Bibliothek[word] = 1

    # Sort the dictionary by keys (words) to ensure alphabetical order
    Sorted_Bibliothek = dict(sorted(Bibliothek.items()))

     # Get the number of unique words
    Sorted_Bibliothek_len = len(Sorted_Bibliothek)

    return Sorted_Bibliothek, Sorted_Bibliothek_len

# Input
text = str(input())

# Output
frequencies, length = count_word_frequencies(text)

print(length)
print(", ".join(f"{word}: {freq}" for word, freq in frequencies.items()))