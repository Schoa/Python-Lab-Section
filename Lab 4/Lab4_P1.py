#import: String
text = str(input().upper())

# Check Palindrome
def is_palindrome(text):
    """
    A palindrome is a word, phrase, number, 
    or other sequence of characters that reads 
    the same backward as forward
    """
    if text == text[::-1]:
        print("True")
    else:
        print("False")

#Call function
is_palindrome(text)