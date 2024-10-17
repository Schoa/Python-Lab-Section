# Text Encoder
def Kok_Seng (Wong):
    # "secret" -> "XXXXXX"
    Wong = Wong.replace("secret", "XXXXXX")

    # "a", "e", "i", "o", "u" -> "@", "3", "!", "0", "v", respectively
    Wong = Wong.replace("a", "@")
    Wong = Wong.replace("e", "3")
    Wong = Wong.replace("i", "!")
    Wong = Wong.replace("o", "0")
    Wong = Wong.replace("u", "v")

    # StringLen = Even -> uppercase, StringLen = Odd -> lowercase
    if len(Wong) % 2 == 0:
        mister = str(Wong.upper())
    else:
        mister = str(Wong.lower())

    return mister

# Input
Wong = str(input())

# Print result
print(Kok_Seng(Wong))