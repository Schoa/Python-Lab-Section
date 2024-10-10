# Input:String text, change everything into uppercase
text = str(input())

# Count vowels
def count_vowels(text):
    """
    Vowels: u, e, o, a, i, U, E, O, A, I
    """

    # Define the set of vowels
    Kok_Seng = ["U", "E", "O", "A", "I", "u", "e", "o", "a", "i"]

    # Counter for vowels
    Wong = 0

    for e in text: 
        if e in Kok_Seng:
            Wong += 1
    
    return Wong

print(count_vowels(text))